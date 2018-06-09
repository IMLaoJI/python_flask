#coding: utf-8
import os
from base64 import b64encode

# SECRET_KEY = os.urandom(24)
SECRET_KEY = '2fRN3ptuiGMqfn4flY4JeXyDN+IDX+/e'

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'sbbs'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SERVER_NAME = 'zlkt.com:5000'


# 邮箱的配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '465'
MAIL_USERNAME = '2413357360@qq.com'
MAIL_PASSWORD = 'ghsnqpxaneujdjdg'
MAIL_DEFAULT_SENDER = '2413357360@qq.com'
MAIL_USE_SSL = True

# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件