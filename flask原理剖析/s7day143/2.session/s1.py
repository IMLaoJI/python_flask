from flask import Flask,session


app = Flask(__name__)
app.secret_key = 'suijksdfsd'


import json
class MySessionInterFace(object):
    def open_session(self,app,request):
        return {}

    def save_session(self, app, session, response):
        response.set_cookie('session_idfsdfsdfsdf',json.dumps(session))

    def is_null_session(self, obj):
        """Checks if a given object is a null session.  Null sessions are
        not asked to be saved.

        This checks if the object is an instance of :attr:`null_session_class`
        by default.
        """
        return False

app.session_interface = MySessionInterFace()

@app.route('/')
def index():
    # 特殊空字典
    # 在local的ctx中找到session
    # 在空字典中写值
    # 在空字典中获取值
    session['xxx'] = 123


    return 'Index'

# # 一旦请求到来
# app.__call__
# app.wsgi_app
# app.session_interface
# app.open_session


if __name__ == '__main__':

    app.run()