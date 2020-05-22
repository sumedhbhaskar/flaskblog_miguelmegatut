from app import app

@app.route('/')
@app.routes('/index')
def index():
    return "Hello World!"
