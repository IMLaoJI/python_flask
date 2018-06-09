from flask import Flask,session
app = Flask(__name__)
app.secret_key = 'sdfsdf'

@app.route('/')
def index():
    # flask内置的使用 加密cookie（签名cookie）来保存数据。
    session['k1'] = 'v1'
    session['k2'] = 'v2'
    return 'xxx'


if __name__ == '__main__':
    app.run()