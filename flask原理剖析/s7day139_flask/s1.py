from flask import Flask

# 实例化Flask对象
app = Flask(__name__)

# 将 '/' 和 函数index的对应关系添加到路由中。
"""
{
    ‘/’:index
}
"""
@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    # 监听用户请求
    # 如果有用户请求到来，则执行app的__call__方法
    # app.__call__
    app.run()