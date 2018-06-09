#encoding: utf-8

from flask import Blueprint
from flask_restful import Resource,marshal_with,fields,Api
from models import Article


bp = Blueprint('article',__name__,url_prefix='/article/')
api = Api(bp)

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

api.add_resource(ArticleView,'<article_id>/',endpoint='article')