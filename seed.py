import faker
from random import randint
from connect import create_connection, database


def generate_fake_data(rows_number):
    fake_data_users = []
    fake_data_tasks = []

    fake_data = faker.Faker()

    for _ in range(rows_number):
        fake_data_users.append((fake_data.name(), fake_data.unique.email()))

        fake_data_tasks.append(
            (
                fake_data.sentence(),
                fake_data.text(),
                randint(1, 3),
                randint(1, rows_number),
            )
        )

    return fake_data_users, fake_data_tasks


sql_to_table_users = """
    INSERT INTO users(fullname,email) VALUES(?,?)
"""
sql_to_table_status = """
    INSERT INTO status(name) VALUES(?)
"""
sql_to_table_tasks = """
    INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?)
"""

users_data, tasks_data = generate_fake_data(10)
if __name__ == "__main__":

    with create_connection(database) as conn:
        cur = conn.cursor()
        cur.executemany(sql_to_table_users, users_data)
        cur.executemany(
            sql_to_table_status, [("new",), ("in progress",), ("completed",)]
        )
        cur.executemany(sql_to_table_tasks, tasks_data)
        conn.commit()
