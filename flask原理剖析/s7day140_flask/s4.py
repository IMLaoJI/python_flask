from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug = True
app.secret_key = 'siuljskdjfs'


@app.before_request
def process_request1(*args,**kwargs):
    print('process_request1 进来了')

@app.before_request
def process_request2(*args,**kwargs):
    print('process_request2 进来了')


@app.after_request
def process_response1(response):
    print('process_response1 走了')
    return response

@app.after_request
def process_response2(response):
    print('process_response2 走了')
    return response



@app.errorhandler(404)
def error_404(arg):
    return "404错误了"


@app.before_first_request
def first(*args,**kwargs):
    pass

@app.route('/index',methods=['GET'])
def index():
    print('index函数')
    return "Index"





if __name__ == '__main__':
    app.run()