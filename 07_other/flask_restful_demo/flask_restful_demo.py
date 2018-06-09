from flask import Flask,render_template,url_for
from flask_restful import Api,Resource,reqparse,inputs

app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        # username
        # password
        from datetime import date
        parser = reqparse.RequestParser()
        parser.add_argument('birthday',type=inputs.date,help='生日字段验证错误！')
        # parser.add_argument('telphone',type=inputs.regex(r'1[3578]\d{9}'))
        # parser.add_argument('home_page',type=inputs.url,help='个人中心链接验证错误！')
        # parser.add_argument('username',type=str,help='用户名验证错误！',required=True)
        # parser.add_argument('password',type=str,help='密码验证错误！')
        # parser.add_argument('age',type=int,help='年龄验证错误！')
        # parser.add_argument('gender',type=str,choices=['male','female','secret'])
        args = parser.parse_args()
        print(args)
        return {"username":"zhiliao"}

api.add_resource(LoginView,'/login/')

# with app.test_request_context():
#     print(url_for('loginview',username='zhiali'))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
