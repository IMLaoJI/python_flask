
# 从flask这个包中导入Flask这个类
# Flask这个类是项目的核心，以后很多操作都是基于这个类的对象
# 注册url、注册蓝图等都是基于这个类的对象
from flask import Flask

# 创建一个Flask对象，传递__name__参数进去
# __name__参数的作用：
# 1. 可以规定模版和静态文件的查找路径
# 2. 以后一些Flask插件，比如Flask-migrate、Flask-SQLAlchemy如果报错了，那么Flask
# 可以通过这个参数找到具体的错误位置
app = Flask(__name__)

# @app.route：是一个装饰器
# @app.route('/')就是将url中的/映射到hello_world这个视图函数上面
# 以后你访问我这个网站的/目录的时候，会执行hello_world这个函数，然后将这个函数的返回值
# 返回给浏览器。
# wwww.baidu.com/ -> hello_world函数
@app.route('/')
def hello_world():
    return '知了课堂'

# www.baidu.com/list/
@app.route('/list/')
def my_list():
    return 'my list'


# 如果这个文件是作为一个主文件运行，那么就执行app.run()方法
# 也就是启动这个网站
if __name__ == '__main__':
    # app.run()：Flask中的一个测试应用服务器
    # while True:
    #   listen()
    #   input()
    app.run(port=8000)
