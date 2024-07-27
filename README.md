## Postgres

### Bring up the postgres DB

```bash
docker-compose up -d
```

### Open postgres shell

```bash
docker-compose exec pg-db psql -U <user> -d <db_name>
```

## Kafka

### (Setup Kafka on local)[https://developer.confluent.io/quickstart/kafka-local/]

### (Python Kafka Client)[https://developer.confluent.io/get-started/python/#introduction]

### install kafka on local machine, only single node is supported

`brew install confluentinc/tap/cli`

### start kafka broker

`confluent local kafka start`

### create a topic

`confluent local kafka topic create <topic_name>`

### write msgs to the topic

`confluent local kafka topic produce <topic_name>`

### Read msgs from kafka topic

`confluent local kafka topic consume quickstart --from-beginning`

### Stop kafka broker

`confluent local kafka stop`
