from flask import Flask, render_template,url_for,redirect,request,Blueprint,current_app,flash

auth = Blueprint('auth',__name__)

@auth.route('/sign',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        t_db = current_app.config['userdb']
        email = request.form['email']
        passwd = request.form['password']
        t_db.signing_up(email,passwd)
        flash('Registration successful','successful')
        return redirect(url_for('auth.signup'))
    else:
        return render_template('signup.html')

@auth.route('/',methods=['POST','GET'])
def login():
    t_db = current_app.config['userdb']
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        t_db.login_in(email,password)
        return redirect(url_for('home'))
    else:
        return render_template('login.html')
