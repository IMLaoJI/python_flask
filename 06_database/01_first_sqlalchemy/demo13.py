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
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer,ForeignKey("user.id"),nullable=False)

    author = relationship("User",backref=backref("articles",cascade="all"),cascade="save-update",single_parent=True,ondelete='')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref="comments")


def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(username='zhiliao')
    article = Article(title='title one')
    article.author = user

    comment = Comment(content='xxx')
    comment.author = user
    session.add(comment)
    session.add(article)

    session.commit()


def operation():
    user = User(username='ketang')
    article = Article(title='abvc')
    article.author = user

    session.add(user)
    session.add(article)


    session.expunge(user)

    session.commit()


if __name__ == '__main__':
    # my_init_db()
    operation()