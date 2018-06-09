from flask import Flask,request,views
from functools import wraps

app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # /settings/?username=xxx
        username = request.args.get('username')
        if username and username == 'zhiliao':
            return func(*args,**kwargs)
        else:
            return '请先登录'
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/settings/')
@login_required
def settings():
    return '这是设置界面'

# login_required(app.route('/settings/')(settings))
#
# app.route('/settings/')(login_required(settings))


class ProfileView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/',view_func=ProfileView.as_view('profile'))


if __name__ == '__main__':
    app.run(debug=True)
