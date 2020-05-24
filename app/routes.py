from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {"username":"sumedh"}
    posts = [
                {
                    "author":{'username':'sumedh'} ,
                     "body":"beautiful sleepless night "
                },
                {
                    "author":{'username':'qikoo'},
                    "body":"a beautiful day "
                }
            ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Yo! you logined with name {}, remember me =  {}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html',title='Sign In',form=form)
