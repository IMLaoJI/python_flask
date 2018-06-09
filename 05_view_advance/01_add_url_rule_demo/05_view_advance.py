from flask import Flask,url_for

app = Flask(__name__)


@app.route('/',endpoint='index')
def hello_world():
    print(url_for('zhiliao'))
    return 'Hello World!'

def my_list():
    return '我是列表页'

app.add_url_rule('/list/',endpoint='zhiliao',view_func=my_list)

# app.test_request_context
# 请求上下文
with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
