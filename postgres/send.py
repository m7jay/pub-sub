import psycopg2
from postgres.db import db_params


def send_notification(channel: str, payload: str):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute(f"NOTIFY {channel}, '{payload}';")
    conn.commit()

    cursor.close()
    conn.close()
