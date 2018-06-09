#encoding: utf-8

from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    deposit = db.Column(db.Float,default=0)
