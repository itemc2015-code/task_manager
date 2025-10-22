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
        #self.db_cursor = self.db.cursor(dictionary=True)

    def show_list(self,user_id):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True,buffered=True)
        c_value = "select * from tasks where auth_id = %s order by date_time desc"
        cursor.execute(c_value,(user_id,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def add_list(self,task_name,user_id):
        cursor = self.db.cursor()
        c_value = ('insert into tasks(tasks,auth_id) values(%s,%s)')
        cursor.execute(c_value,(task_name,user_id))
        self.db.commit()
        cursor.close()

    def del_list(self,task_delete):
        cursor = self.db.cursor()
        c_value = ('delete from tasks where no = %s ')
        cursor.execute(c_value,(task_delete,))
        self.db.commit()
        cursor.close()

    def get_task(self,no):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True,buffered=True)
        c_value = ('select * from tasks where no = %s')
        cursor.execute(c_value,(no,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def update_list(self,task_update,no):
        cursor = self.db.cursor()
        c_value = ('update tasks set tasks = %s where no = %s')
        cursor.execute(c_value,(task_update,no))
        self.db.commit()
        cursor.close()

class UserDB(TaskDB):

    def signing_up(self,email,hash_pass):
        cursor = self.db.cursor()
        c_value = 'insert into auth(username,pwd) values(%s,%s) '
        cursor.execute(c_value,(email,hash_pass))
        self.db.commit()
        cursor.close()

    def login_in(self,email):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True,buffered=True)
        c_value =  'select * from auth where username = %s'
        cursor.execute(c_value,(email,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # def login_in(self,email,password):
    #     self.db.ping(reconnect=True)
    #     cursor = self.db.cursor(dictionary=True,buffered=True)
    #     c_value =  'select * from auth where username = %s and pwd = %s'
    #     cursor.execute(c_value,(email,password))
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return result

    # def get_email(self,g_email):
    #     self.db.ping(reconnect=True)
    #     cursor = self.db.cursor(dictionary=True,buffered=True)
    #     c_value = 'select * from auth where username = %s'
    #     cursor.execute(c_value,(g_email,))
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return result



