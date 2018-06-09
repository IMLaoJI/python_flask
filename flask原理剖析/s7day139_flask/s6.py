from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = "asdfasdf"

# @app.route('/',methods=['GET','POST'],endpoint='n1',defaults={'nid':888})
# def index(nid):
#     print(nid)
#     return 'Hello World!'
#
#
# def login():
#     return '登录'
# app.add_url_rule('/login', 'n2', login, methods=['GET',"POST"])


@app.route('/index',methods=['GET','POST'],endpoint='n1',redirect_to="/index2")
def index():
    return '公司老首页'


@app.route('/index2',methods=['GET','POST'],endpoint='n2')
def index2():
    return '公司新首页'




if __name__ == '__main__':
    app.run()