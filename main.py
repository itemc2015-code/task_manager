from flask import Flask,render_template, request, redirect,url_for, flash
import taskmngr_db
from actions import action
from auth import auth
from taskmngr_db import TaskDB, UserDB

app = Flask(__name__)
app.secret_key = "mysecretkey"

app.config['taskdb'] = TaskDB()
app.config['userdb'] = UserDB()

app.register_blueprint(action,url_prefix='/')
app.register_blueprint(auth,url_prefix='/')

@app.route('/login',methods=['POST','GET'])
def home():
    t_db = app.config['taskdb']
    if request.method == "POST":
        task_name = request.form.get('content')
        t_db.add_list(task_name)
        return redirect(url_for('home'))
    else:
        task_list = t_db.show_list()
        return render_template('main.html',task_list=task_list)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

'''
user login
flash
encrypt pass
'''


