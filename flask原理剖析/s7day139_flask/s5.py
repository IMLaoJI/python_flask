from flask import Flask,views

app = Flask(__name__)
app.debug = True
app.secret_key = "asdfasdf"


def auth(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner

class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [auth, ]

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'

app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))  # name=endpoint


if __name__ == '__main__':
    app.run()