from sqlite3 import Error
from connect import create_connection, database

sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
    );
"""


sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
    );
"""

sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (status_id) REFERENCES status (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
"""


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


with create_connection(database) as conn:
    if conn is None:
        print("problem with creating database")

    else:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_status_table)
        create_table(conn, sql_create_tasks_table)
