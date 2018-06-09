#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .models import *
from .views import account

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')

    # 将db注册到app中
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(account.account)


    return app
