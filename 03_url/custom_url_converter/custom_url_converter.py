from flask import Flask,url_for
from werkzeug.routing import BaseConverter


app = Flask(__name__)

# 一个url中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式
class TelephoneConveter(BaseConverter):
    regex = r'1[85734]\d{9}'

# 用户在访问/posts/a+b/
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return "+".join(value)
        # return "hello"

app.url_map.converters['tel'] = TelephoneConveter
app.url_map.converters['list'] = ListConverter

@app.route('/')
def hello_world():
    print('='*30)
    print(url_for('posts',boards=['a','b']))
    print('='*30)
    return 'Hello World!'

@app.route('/user/<string:user_id>/')
def user_profile(user_id):
    return '您输入的user_id为：%s' % user_id

@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return '您的手机号码是：%s' % my_tel

@app.route('/posts/<list:boards>/')
def posts(boards):
    print(boards)
    return "您提交的板块是：%s" % boards


if __name__ == '__main__':
    app.run(debug=True)
