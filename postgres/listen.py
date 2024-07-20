import psycopg2
import select
from postgres.db import db_params


def listen_notifications(channel: str):
    conn = psycopg2.connect(**db_params)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"LISTEN {channel};")
    print(f"Waiting for notifications on channel '{channel}'...")

    while True:
        if select.select([conn], [], [], 5) == ([], [], []):
            print("Timeout. No notifications.")
        else:
            conn.poll()
            while conn.notifies:
                notify = conn.notifies.pop(0)
                print(f"Got NOTIFY: {notify.channel} - {notify.payload}")
