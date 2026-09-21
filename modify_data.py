from seed import tasks_data
from select_data import execute_queries

sql_update_status = """UPDATE tasks 
SET status_id = ? 
WHERE user_id = ?;"""
sql_add_new_task = (
    """INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?);"""
)
sql_delete_task_by_id = """DELETE FROM tasks WHERE id = ?;"""
sql_udate_user_name = """UPDATE users
SET fullname = ?
WHERE id = ?;"""


# def modify_database(sql_query):
#     try:
#         c = conn.cursor()
#         c.execute(sql_query)
#         conn.commit()
#     except Error as e:
#         print(e)


# with create_connection(database) as conn:
#     if conn is None:
#         print("problem with creating database")
#     # modify_database(sql_update_status)
#     # modify_database()

execute_queries(sql_update_status, 1, 2, is_modify=True)
execute_queries(
    sql_add_new_task, tasks_data[0][0], tasks_data[0][1], 3, 2, is_modify=True
)
execute_queries(sql_delete_task_by_id, 1, is_modify=True)
execute_queries(sql_udate_user_name, "Alex Dou", 1, is_modify=True)
# if __name__ == "__main__":
#     print(f"title = {tasks_data[0][0]}")
#     print(f"descr = {tasks_data[0][1]}")
