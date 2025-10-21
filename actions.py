from flask import Blueprint,url_for,render_template,request,redirect,current_app
import taskmngr_db

action = Blueprint('action',__name__)

@action.route('/delete/<int:no>')
def del_list(no):
    t_db = current_app.config['taskdb']
    t_db.del_list(no)
    return redirect(url_for('task'))

@action.route('/update/<int:no>', methods=['POST','GET'])
def up_list(no):
    t_db = current_app.config['taskdb']
    if request.method == "POST":
        task_update = request.form.get('content')
        t_db.update_list(task_update,no)
        return redirect(url_for('task'))
    else:
        task = t_db.get_task(no)
        return render_template('update.html',task=task)
