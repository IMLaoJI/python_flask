#coding: utf8

from exts import db
from werkzeug.security import generate_password_hash

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    deposit = db.Column(db.Float,default=0) # 薪水