import psycopg2 as ps
from decouple import config


db_url = config("DATABASE_URL")


def get_connection():
    return ps.connect(db_url)