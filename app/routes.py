from app import app
from flask import render_template

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
