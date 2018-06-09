from flask import Flask,request,Response
from datetime import datetime,timedelta
from cmsviews import bp

app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'hy.com:5000'

@app.route('/')
def hello_world():
    resp = Response("知了课堂")
    expires = datetime(year=2017,month=12,day=11,hour=16,minute=0,second=0)
    # 使用expires参数，就必须使用格林尼治时间
    # 要相对北京时间少8个小时
    expires = datetime.now() + timedelta(days=30,hours=16)
    # 在新版本的http协议中，expires参数视为被废弃
    # max_age，在IE8一下的浏览器中是不支持的
    # resp.set_cookie('username','zhiliao',expires=expires,max_age=60)
    resp.set_cookie('username','zhiliao',domain='.hy.com')
    return resp

@app.route('/del/')
def delete_cookie():
    resp = Response("删除cookie")
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
