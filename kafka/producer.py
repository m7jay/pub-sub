#!/usr/bin/env python

from random import choice
from confluent_kafka import Producer
from settings import KAFKA_BROKER_URL, KAFKA_TOPIC

# +-----------------+-------+
# | Kafka REST Port | 8082  |
# | Plaintext Ports | 52970 |
# +-----------------+-------+

if __name__ == "__main__":

    config = {
        "bootstrap.servers": KAFKA_BROKER_URL,
        # Fixed properties
        "acks": "all",
    }

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print("ERROR: Message failed delivery: {}".format(err))
        else:
            print(
                "Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(),
                    key=msg.key().decode("utf-8"),
                    value=msg.value().decode("utf-8"),
                )
            )

    # Produce data by selecting random values from these lists.
    topic = KAFKA_TOPIC
    user_ids = ["eabara", "jsmith", "sgarcia", "jbernard", "htanaka", "awalther"]
    products = ["book", "alarm clock", "t-shirts", "gift card", "batteries"]

    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
