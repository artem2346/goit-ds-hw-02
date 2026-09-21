from sqlite3 import Error

from connect import create_connection, database

sql_select_tasks_by_user_id = """SELECT * FROM tasks WHERE user_id = ?;"""
sql_select_tasks_by_status = (
    """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = ?);"""
)
sql_select_list_users_without_tasks = (
    """SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);"""
)
sql_select_task_not_complited = """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name != 'completed');"""
sql_select_users_by_emails = """SELECT * FROM users WHERE email LIKE ?;"""
sql_select_count_tasks_by_status = """SELECT COUNT(tasks.id) as total_tasks, s.name AS task_status FROM tasks FULL JOIN status AS s ON s.id = tasks.status_id GROUP BY tasks.status_id;"""
sql_select_tasks_by_domen_email = """SELECT tasks.title AS title, tasks.description AS description, u.email AS emails FROM tasks INNER JOIN users AS u ON u.id = tasks.user_id WHERE u.email LIKE ?;"""
sql_select_tasks_without_descr = """SELECT * FROM tasks WHERE description NOT NULL;"""
sql_select_users_by_status_in_progress = """SELECT s.name AS status,u.fullname AS name,tasks.title AS title, tasks.description AS description FROM tasks INNER JOIN users AS u ON u.id = tasks.user_id INNER JOIN status AS s ON s.id = tasks.status_id WHERE s.name = 'in progress';"""
sql_select_users_with_count_tasks = """SELECT COUNT(t.id) AS count_tasks,users.fullname AS name,users.email AS email FROM users LEFT JOIN tasks AS t ON t.user_id = users.id GROUP BY users.id;"""

# def select_tasks_by_user_id(user_id):
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute("""SELECT * FROM tasks WHERE user_id = ?;""", (user_id,))
#         rows = cur.fetchall()
#         return rows


# def select_tasks_by_status(status):
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name = ?);""",
#             (status,),
#         )
#         rows = cur.fetchall()
#         return rows


# def select_list_users_without_tasks():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);"""
#         )
#         rows = cur.fetchall()
#         return rows


# def select_task_not_complited():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT * FROM tasks WHERE status_id IN (SELECT id FROM status WHERE name != 'completed');"""
#         )
#         rows = cur.fetchall()
#         return rows


# def select_users_by_emails(email):
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute("""SELECT * FROM users WHERE email LIKE ?;""", (email,))
#         rows = cur.fetchall()
#         return rows


# def select_count_tasks_by_status():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT COUNT(tasks.id) as total_tasks, s.name AS task_status FROM tasks FULL JOIN status AS s ON s.id = tasks.status_id GROUP BY tasks.status_id;"""
#         )
#         rows = cur.fetchall()
#         return rows


# def select_tasks_by_domen_email(email_domen):
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT tasks.title AS title, tasks.description AS description, u.email AS emails FROM tasks INNER JOIN users AS u ON u.id = tasks.user_id WHERE u.email LIKE ?;""",
#             (email_domen,),
#         )
#         rows = cur.fetchall()
#         return rows


# def select_tasks_without_descr():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute("""SELECT * FROM tasks WHERE description NOT NULL;""")
#         rows = cur.fetchall()
#         return rows


# def select_users_by_status_in_progress():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT s.name AS status,u.fullname AS name,tasks.title AS title, tasks.description AS description FROM tasks INNER JOIN users AS u ON u.id = tasks.user_id INNER JOIN status AS s ON s.id = tasks.status_id WHERE s.name = 'in progress';"""
#         )
#         rows = cur.fetchall()
#         return rows


# def select_users_with_count_tasks():
#     with create_connection(database) as conn:
#         cur = conn.cursor()
#         cur.execute(
#             """SELECT COUNT(t.id) AS count_tasks,users.fullname AS name,users.email AS email FROM users LEFT JOIN tasks AS t ON t.user_id = users.id GROUP BY users.id;"""
#         )
#         rows = cur.fetchall()
#         return rows


def execute_queries(sql_query, *args, is_modify=False):
    try:
        with create_connection(database) as conn:
            cur = conn.cursor()
            if args:
                cur.execute(sql_query, args)
            else:
                cur.execute(sql_query)

            if is_modify == False:
                rows = cur.fetchall()
                return rows
            else:
                conn.commit()
                return None
    except Error as e:
        print(e)


execute_queries(sql_select_tasks_by_user_id, 5)
execute_queries(sql_select_tasks_by_status, "completed")
execute_queries(sql_select_list_users_without_tasks)
execute_queries(sql_select_task_not_complited)
execute_queries(sql_select_users_by_emails, "coopersusan@example.org")
execute_queries(sql_select_count_tasks_by_status)
execute_queries(sql_select_tasks_by_domen_email, "%@example.com")
execute_queries(sql_select_tasks_without_descr)
execute_queries(
    sql_select_users_by_status_in_progress,
)
execute_queries(sql_select_users_with_count_tasks)


# if __name__ == "__main__":
#     execute_queries(sql_select_tasks_by_user_id, 5)
#     execute_queries(sql_select_tasks_by_status, "completed")
#     execute_queries(sql_select_list_users_without_tasks)
#     execute_queries(sql_select_task_not_complited)
#     execute_queries(sql_select_users_by_emails, "coopersusan@example.org")
#     execute_queries(sql_select_count_tasks_by_status)
#     execute_queries(sql_select_tasks_by_domen_email, "%@example.com")
#     execute_queries(sql_select_tasks_without_descr)
#     execute_queries(
#         sql_select_users_by_status_in_progress,
#     )
#     execute_queries(sql_select_users_with_count_tasks)
