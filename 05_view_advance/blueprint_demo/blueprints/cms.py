#encoding: utf-8

from flask import Blueprint

cms_bp = Blueprint('cms',__name__,subdomain='cms')

@cms_bp.route('/')
def index():
    return 'cms index page'