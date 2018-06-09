from flask import Flask,request,g,template_rendered,render_template,got_request_exception
from blinker import Namespace
from signals import login_signal

# Namespace：命名空间
# 1. 定义信号
# zlspace = Namespace()
# fire_signal = zlspace.signal('fire')
#
# # 2. 监听信号
# def fire_bullet(sender):
#     print(sender)
#     print('start fire bullet')
# fire_signal.connect(fire_bullet)
#
# # 3. 发送一个信号
# fire_signal.send()


# 定义一个登录的信号，以后用户登录进来以后
# 就发送一个登录信号，然后能够监听这个信号
# 在监听到这个信号以后，就记录当前这个用户登录的信息
# 用信号的方式，记录用户的登录信息


app = Flask(__name__)

# def template_rendered_func(sender,template,context):
#     print('sender:',sender)
#     print('template:',template)
#     print('context:',context)
# template_rendered.connect(template_rendered_func)

def request_exception_log(sender,exception):
    print(exception)
got_request_exception.connect(request_exception_log)

@app.route('/')
def hello_world():
    a = 1/0
    return render_template('index.html')

@app.route('/login/')
def login():
    # 通过查询字符串的形式来传递username这个参数
    username = request.args.get('username')
    if username:
        g.username = username
        login_signal.send()
        return '登录成功！'
    else:
        return '请输入用户名！'

if __name__ == '__main__':
    app.run(debug=True)
