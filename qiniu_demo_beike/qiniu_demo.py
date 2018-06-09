from flask import Flask,jsonify,render_template
import qiniu


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/uptoken/')
def uptoken():
    access_key = 'M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL'
    secret_key = '7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4'
    q = qiniu.Auth(access_key,secret_key)
    bucket = 'hyvideo'
    token = q.upload_token(bucket)
    return jsonify({"uptoken":token})


if __name__ == '__main__':
    app.run(debug=True)
