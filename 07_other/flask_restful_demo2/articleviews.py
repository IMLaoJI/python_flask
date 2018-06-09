#encoding: utf-8

from flask import Blueprint,render_template,make_response
from flask_restful import Api,Resource,fields,marshal_with
from models import Article

article_bp = Blueprint('article',__name__,url_prefix='/article')
api = Api(article_bp)

@api.representation('text/html')
def output_html(data,code,headers):
    print(data)
    # 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp

class ArticleView(Resource):

    resource_fields = {
        'aritlce_title':fields.String(attribute='title'),
        'content':fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String
        })),
        'read_count': fields.Integer(default=80)
    }

    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article
# /article/article/1/
api.add_resource(ArticleView,'/<article_id>/',endpoint='article')


class ListView(Resource):
    def get(self):
        return render_template('index.html')
api.add_resource(ListView,'/list/',endpoint='list')