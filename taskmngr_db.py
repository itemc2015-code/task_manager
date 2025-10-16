import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class TaskDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv('db_host'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            database=os.getenv('db_database')
        )
        self.db_cursor = self.db.cursor(dictionary=True)

    def show_list(self):
        self.db_cursor.execute("select * from tasks order by date_time desc")
        return self.db_cursor.fetchall()

    def add_list(self,task_name):
        c_value = ('insert into tasks(tasks) values(%s)')
        self.db_cursor.execute(c_value,(task_name,))
        self.db.commit()

    def del_list(self,task_delete):
        c_value = ('delete from tasks where no = %s ')
        self.db_cursor.execute(c_value,(task_delete,))
        self.db.commit()

    def get_task(self,no):
        c_value = ('select * from tasks where no = %s')
        self.db_cursor.execute(c_value,(no,))
        return self.db_cursor.fetchone()

    def update_list(self,task_update,no):
        c_value = ('update tasks set tasks = %s where no = %s')
        self.db_cursor.execute(c_value,(task_update,no))
        self.db.commit()

class UserDB(TaskDB):

    def signing_up(self,email,passwd):
        c_value = 'insert into auth(username,pwd) values(%s,%s) '
        self.db_cursor.execute(c_value,(email,passwd))
        self.db.commit()



