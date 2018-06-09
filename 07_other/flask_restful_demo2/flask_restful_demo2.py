from flask import Flask
import config
from exts import db
from models import User,Article,Tag
from articleviews import article_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(article_bp)
# api = Api(app)

#1. flask-restful结合蓝图使用
#2. 使用flask-restful渲染模版


# class Article(object):
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content
#
# article = Article(title='abc',content='sfasdfsdfsdafsad')
#
# class ArticleView(Resource):
#
#     resource_fields = {
#         'title': fields.String,
#         'content': fields.String
#     }
#
#     # restful规范中，要求，定义好了返回的参数
#     # 即使这个参数没有值，也应该返回，返回一个None回去
#
#     @marshal_with(resource_fields)
#     def get(self):
#         return article
#
# api.add_resource(ArticleView,'/article/',endpoint='article')



@app.route('/')
def hello_world():
    user = User(username='zhiliao',email='xxx@qq.com')
    article = Article(title='abc',content='123')
    article.author = user
    tag1 = Tag(name='前端')
    tag2 = Tag(name='Python')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
