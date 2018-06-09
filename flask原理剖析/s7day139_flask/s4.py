from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = "asdfasdf"

"""
1. decorator = app.route('/',methods=['GET','POST'],endpoint='n1')
    def route(self, rule, **options):
        # app对象
        # rule= /
        # options = {methods=['GET','POST'],endpoint='n1'}
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
2. @decorator
    decorator(index)
"""
@app.route('/',methods=['GET','POST'],endpoint='n1')
def index():
    return 'Hello World!'


def login():
    return '登录'

app.add_url_rule('/login', 'n2', login, methods=['GET',"POST"])


if __name__ == '__main__':
    app.run()