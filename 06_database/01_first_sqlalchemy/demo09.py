#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func,and_,or_,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
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

# 父表 / 从表
# user/article

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref="users",uselist=False)

    def __repr__(self):
        return "<Article(title:%s,content:%s)>" % (self.title,self.content)

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='zhiliao')
# session.add(user)
# session.commit()
#
# article = Article(title='abc',content='123',uid=1)
# session.add(article)
# session.commit()
#
# # 现在是基于demo08的代码来的，就是有两个表，分别为user和article，他们俩之间存在一个外键关系
# article = session.query(Article).first()
# uid = article.uid
# print(article)
# user = session.query(User).get(uid)
# print(user)

user = session.query(User).first()
session.delete(user)
session.commit()