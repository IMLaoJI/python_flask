from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list/')
def article_list():
    return 'article list'

@app.route('/p/<float:article_id>')
def article_detail(article_id):
    return '您请求的文章是：%s' % article_id


# @app.route('/article/<path:test>/')
# def test_article(test):
#     return 'test article：%s' % test

@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '用户个人中心页面：%s' % user_id

# /blog/<id>/
# /user/<id>/
@app.route('/<any(blog,article):url_path>/<id>/')
def detail(url_path,id):
    if url_path == 'blog':
        return '博客详情：%s' % id
    else:
        return '博客详情：%s' % id

# 通过问号的形式传递参数
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    print('ie:',ie)
    return '您通过查询字符串的方式传递的参数是：%s' % wd

# import uuid
# print(uuid.uuid4())

if __name__ == '__main__':
    app.run(debug=True)
