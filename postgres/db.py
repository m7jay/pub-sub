from postgres.settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

db_params = {
    "dbname": POSTGRES_DB,
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "host": "localhost",
    "port": "5432",
}
