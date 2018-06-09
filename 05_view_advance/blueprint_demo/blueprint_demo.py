from flask import Flask,url_for,render_template
from blueprints.user import user_bp
from blueprints.news import news_bp
from blueprints.cms import cms_bp

app = Flask(__name__)
app.config['SERVER_NAME'] = 'jd.com:5000'
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)

# 用户模块
# 新闻模块
# 电影模块
# 读书模块

# IP地址是不能有子域名的
# cms.127.0.0.1:5000
# localhost也是不能有子域名的

@app.route('/')
def hello_world():
    print(url_for('news.news_list'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
