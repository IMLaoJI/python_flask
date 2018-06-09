from flask import Flask
import config

app = Flask(__name__)
# dict
# a = {'a':1}
# b = {'b':2}
# a.update(b=2)
# print(a)
# 设置配置参数的形式
# DEBUG必须要大写，不能小写
app.config.from_object(config)

@app.route('/')
def hello_world():
    a = 1
    b = 0
    print('hello zhiliao')
    c = a/b
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
