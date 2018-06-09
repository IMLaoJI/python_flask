#coding: utf8
import os

DB_URI = 'mysql+pymysql://root:root@localhost:3306/icbc?charset=utf8'

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)

SERVER_NAME = 'icbc.com'