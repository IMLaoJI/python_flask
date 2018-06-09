#encoding: utf-8

from flask import Blueprint

user_bp = Blueprint('user',__name__,url_prefix='/user')

# 个人中的url与视图函数
@user_bp.route('/profile/')
def profile():
    return '个人中心页面'

@user_bp.route('/settings/')
def settings():
    return '个人设置页面'