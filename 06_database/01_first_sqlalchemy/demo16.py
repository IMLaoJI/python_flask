#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func,and_,or_,ForeignKey,Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
# 在Python3中才有这个enum模块，在python2中没有
import enum
from datetime import datetime
import random

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50),nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref=backref("articles",lazy="dynamic"))

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhilio')
# for x in range(100):
#     article = Article(title="title %s" % x)
#     article.author = user
#     session.add(article)
# session.commit()

from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.dynamic import AppenderQuery
from sqlalchemy.orm.query import Query
user = session.query(User).first()
# 是一个Query对象。
# print(user.articles.filter(Article.id > 50).all())
# 可以继续追加数据进去
article =Article(title='title 100')
user.articles.append(article)
session.commit()