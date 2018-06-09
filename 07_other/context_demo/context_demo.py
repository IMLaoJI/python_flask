from flask import Flask,request,session,url_for,current_app,g,render_template,abort
from werkzeug.local import Local,LocalStack
from utils import log_a,log_b,log_c
from threading import local
import os

# 只要绑定在Local对象上的属性
# 在每个线程中都是隔离的
# Thread Local


# flask=werkzeug+sqlalchemy+jinja

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 栈

# with app.app_context():
#     print(current_app.name)

@app.route('/')
def index():
    # print(current_app.name)
    # print(url_for('my_list'))
    username = request.args.get('username')
    g.username = username
    # log_a()
    # log_b()
    # log_c()
    print(g.user)
    if hasattr(g,'user'):
        print(g.user)
    return render_template('index.html')

@app.route('/list/')
def my_list():
    session['user_id'] = 1
    user_id = request.args.get('user_id')
    if user_id == '1':
        return 'hello'
    else:
        # 如果user_id在数据库中不存在，这时候我就让他跳转到400错误
        abort(400)
    return render_template('list.html')

with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for('my_list'))


# @app.before_first_request
# def first_request():
#     print('hello world')

@app.before_request
def before_request():
    # print('在视图函数执行之前执行的钩子函数')
    user_id = session.get('user_id')
    if user_id:
        g.user = 'zhiliao'

@app.context_processor
def context_processor():
    # return {"current_user":'zhiliao'}
    if hasattr(g,'user'):
        return {"current_user":g.user}
    else:
        return {}


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@app.errorhandler(400)
def args_error(error):
    return '您的参数不正确'

if __name__ == '__main__':
    app.run(debug=True)