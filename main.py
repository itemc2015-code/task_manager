from flask import Flask,render_template, request, redirect,url_for
import taskmngr_db

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == "POST":
        task_name = request.form['content']
        taskmngr_db.add_list(task_name)
        return redirect(url_for('home'))
    else:
        task_list = taskmngr_db.show_list()
        return render_template('main.html',task_list=task_list)

@app.route('/delete/<int:no>')
def del_list(no):
    taskmngr_db.del_list(no)
    return redirect(url_for('home'))

@app.route('/update/<int:no>', methods=['POST','GET'])
def up_list(no):
    if request.method == "POST":
        task_update = request.form['content']
        taskmngr_db.update_list(task_update,no)
        return redirect(url_for('home'))
    else:
        task = taskmngr_db.get_task(no)
        return render_template('update.html',task=task)

if __name__ == "__main__":
    app.run(debug=True)

'''
change to .get
.env
user login
blueprint
flash
encrypt pass
'''


