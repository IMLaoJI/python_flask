#encoding: utf-8

from flask import Blueprint,render_template,url_for

news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='zhiliao',static_folder='zhiliao_static')

@news_bp.route('/list/')
def news_list():
    print(url_for('news.news_detail'))
    return render_template('news_list.html')

@news_bp.route('/detail/')
def news_detail():
    return '新闻详情页面'
