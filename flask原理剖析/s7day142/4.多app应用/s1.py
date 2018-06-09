from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, current_app

app1 = Flask('app01')

app2 = Flask('app02')



@app1.route('/index')
def index():
    return "app01"


@app2.route('/index2')
def index2():
    return "app2"

# http://www.oldboyedu.com/index
# http://www.oldboyedu.com/sec/index2
dm = DispatcherMiddleware(app1, {
    '/sec': app2,
})

if __name__ == "__main__":
    app2.__call__
    run_simple('localhost', 5000, dm)