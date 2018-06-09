#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BaseConfig(object):
    # SESSION_TYPE = 'redis'  # session类型为redis
    # SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    # SESSION_PERMANENT = True  # 如果设置为False，则关闭浏览器session就失效。
    # SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3306/s7day145_2?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass
