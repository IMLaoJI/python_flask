#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint
from .. import db
from .. import models

account = Blueprint('account', __name__)


@account.route('/login')
def login():
    # 添加示例
    """
    db.session.add(models.Users(username='alex', pwd='123', gender=1))
    db.session.commit()

    obj = db.session.query(models.Users).filter(models.Users.id == 1).first()
    print(obj)

    PS: db.session和db.create_session
    """
    # db.session.add(models.Users(username='wupeiqi1', email='wupeiqi1@xx.com'))
    # db.session.commit()
    # db.session.close()
    #
    # db.session.add(models.Users(username='wupeiqi2', email='wupeiqi2@xx.com'))
    # db.session.commit()
    # db.session.close()
    # db.session.add(models.Users(username='alex1',email='alex1@live.com'))
    # db.session.commit()
    # db.session.close()



    user_list = db.session.query(models.Users).all()
    db.session.close()
    for item in user_list:
        print(item.username)


    return 'login'
