from flask import Flask,session,Session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

@app.route('/')
def index():
    session['username'] = 'zhiliao'
    session['user_id'] = '123'
    # permanent：持久化
    session.permanent = True
    print(type(session))
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')
    print(user_id)
    return username or '没有session'

@app.route('/delete_session/')
def delete_session():
    # session.pop('username')
    session.clear()
    return '删除成功'


if __name__ == '__main__':
    app.run(debug=True)
