from flask import Blueprint,url_for,render_template,request,redirect
import taskmngr_db

action = Blueprint('action',__name__)

@action.route('/delete/<int:no>')
def del_list(no):
    taskmngr_db.del_list(no)
    return redirect(url_for('home'))

@action.route('/update/<int:no>', methods=['POST','GET'])
def up_list(no):
    if request.method == "POST":
        task_update = request.form.get('content')
        taskmngr_db.update_list(task_update,no)
        return redirect(url_for('home'))
    else:
        task = taskmngr_db.get_task(no)
        return render_template('update.html',task=task)
