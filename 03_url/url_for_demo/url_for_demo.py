from flask import Flask,url_for,request

app = Flask(__name__)

# /  =>   hello_world
# hello_world   => /

@app.route('/')
def hello_world():
    # /list/
    # /list/1/
    # return 'Hello World'
    return url_for('login',next='/')
    # /login/?next=/
    # return '/post/list/1/'

@app.route('/login/')
def login():
    return 'login'

@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'

@app.route('/post/detail/<id>/')
def detail():
    return 'detail'

if __name__ == '__main__':
    app.run(debug=True)
