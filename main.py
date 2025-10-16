from flask import Flask,render_template, request, redirect,url_for
import taskmngr_db
from actions import action
from taskmngr_db import TaskDB

app = Flask(__name__)

app.config['taskdb'] = TaskDB()

app.register_blueprint(action,url_prefix='/')

@app.route('/',methods=['POST','GET'])
def home():
    t_db = app.config['taskdb']
    if request.method == "POST":
        task_name = request.form.get('content')
        t_db.add_list(task_name)
        return redirect(url_for('home'))
    else:
        task_list = t_db.show_list()
        return render_template('main.html',task_list=task_list)

@app.route('/sign')
def signup():
    return render_template('signup.html')

@app.route('/log')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

'''
user login
flash
encrypt pass
'''


