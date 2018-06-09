from flask import Flask,signals,render_template

app = Flask(__name__)

# 往信号中注册函数
def func(*args,**kwargs):
    print('触发型号',args,kwargs)
signals.request_started.connect(func)

# 触发信号： signals.request_started.send()

@app.before_first_request
def before_first1(*args,**kwargs):
    pass
@app.before_first_request
def before_first2(*args,**kwargs):
    pass

@app.before_request
def before_first3(*args,**kwargs):
    pass



@app.route('/',methods=['GET',"POST"])
def index():
    print('视图')
    return render_template('index.html')


if __name__ == '__main__':
    app.wsgi_app
    app.run()