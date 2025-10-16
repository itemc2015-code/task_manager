import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv('db_host'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password'),
    database=os.getenv('db_database')
)
db_cursor = db.cursor(dictionary=True)

def show_list():
    db_cursor.execute("select * from tasks order by date_time desc")
    return db_cursor.fetchall()

def add_list(task_name):
    c_value = ('insert into tasks(tasks) values(%s)')
    db_cursor.execute(c_value,(task_name,))
    db.commit()

def del_list(task_delete):
    c_value = ('delete from tasks where no = %s ')
    db_cursor.execute(c_value,(task_delete,))
    db.commit()

def get_task(no):
    c_value = ('select * from tasks where no = %s')
    db_cursor.execute(c_value,(no,))
    return db_cursor.fetchone()

def update_list(task_update,no):
    c_value = ('update tasks set tasks = %s where no = %s')
    db_cursor.execute(c_value,(task_update,no))
    db.commit()

