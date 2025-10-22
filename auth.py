from flask import Flask, render_template,url_for,redirect,request,Blueprint,current_app,flash,session
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/sign',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        t_db = current_app.config['userdb']
        email = request.form['email']
        passwd = request.form['password']
        confirm = request.form['confirm']
        if len(email) == 0:
            flash('Email address cannot be empty','error')
            return redirect(url_for('auth.signup'))
        elif len(passwd) == 0:
            flash('Password cannot be empty','error')
            return redirect(url_for('auth.signup'))
        elif passwd != confirm:
            flash('Password not match','error')
            return redirect(url_for('auth.signup'))
        else:
            hash_pass = generate_password_hash(passwd)
            t_db.signing_up(email,hash_pass)
            flash('Registration successful','success')
            return redirect(url_for('auth.signup'))
    else:
        return render_template('signup.html')

@auth.route('/',methods=['POST','GET'])
def login():
    t_db = current_app.config['userdb']
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user_email = t_db.login_in(email)
        if user_email and check_password_hash(user_email['pwd'],password):
            flash('Login successfully','success')
            session['user_id']= user_email['no']
            return redirect(url_for('task'))
        else:
            flash('Invalid login', 'error')
            return render_template('login.html')
    else:
        return render_template('login.html')

@auth.route('/logout')
def logout():
    user_id = session.get('user_id')
    if user_id:
        session.clear()
        flash('You have been logged out','success')
        return redirect(url_for('auth.login'))
    else:
        flash('Invalid','error')
        return redirect(url_for('auth.login'))
