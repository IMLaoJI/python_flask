#encoding: utf-8

from flask_restful import Api,Resource
from flask import Blueprint,make_response,render_template

user_bp = Blueprint('user',__name__,url_prefix='/user')
api = Api(user_bp)

@api.representation('text/html')
def output_html(data,code,headers):
    resp = make_response(data)
    return resp

class UserView(Resource):
    def get(self):
        return render_template('user.html')

    def post(self):
        return "hello"

api.add_resource(UserView,'/list/',endpoint='user')