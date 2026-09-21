import sqlite3
from contextlib import contextmanager

database = "database.db"


@contextmanager
def create_connection(df_file):
    try:
        conn = sqlite3.connect(df_file)
        yield conn
    except Exception as ex:
        conn.rollback()
        raise Exception(ex)
    finally:
        conn.close()
