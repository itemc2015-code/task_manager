from flask import Flask,render_template, request, redirect,url_for, flash,session
from actions import action
from auth import auth
from taskmngr_db import TaskDB, UserDB

app = Flask(__name__)
app.secret_key = "mysecretkey"

app.config['taskdb'] = TaskDB()
app.config['userdb'] = UserDB()

app.register_blueprint(action,url_prefix='/')
app.register_blueprint(auth,url_prefix='/')
print(app.url_map)

@app.route('/task',methods=['POST','GET'])
def task():
    t_db = app.config['taskdb']
    session.get('user_id')
    if request.method == "POST":
        task_name = request.form.get('content')
        t_db.add_list(task_name)
        return redirect(url_for('task'))
    else:
        task_list = t_db.show_list()
        return render_template('main.html',task_list=task_list)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)



