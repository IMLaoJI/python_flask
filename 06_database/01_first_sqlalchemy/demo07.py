#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func,and_,or_
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)
    content = Column(Text)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# session.query(Article).filter(Article.id == 1)
# session.query(Article).filter_by(id = 1)

# 1. equal
# article = session.query(Article).filter(Article.title == "title0").first()
# print(article)

# 2. not equal
# articles = session.query(Article).filter(Article.title != 'title0').all()
# print(articles)

# 3. like & ilike（不区分大小写）
# articles = session.query(Article).filter(Article.title.ilike('title%')).all()
# print(articles)

# 4. in：
# for xxx in xxx
# def _in()
# articles = session.query(Article).filter(Article.title.in_(['title1','title2'])).all()
# print(articles)

# not in
# articles = session.query(Article).filter(~Article.title.in_(['title1','title2'])).all()
# print(articles)
# articles = session.query(Article).filter(Article.title.notin_(['title1','title2'])).all()
# print(articles)

# is null
# articles = session.query(Article).filter(Article.content==None).all()
# print(articles)

# is not null
# articles = session.query(Article).filter(Article.content!=None).all()
# print(articles)

# and
# articles = session.query(Article).filter(Article.title=='abc',Article.content=='abc').all()
# print(articles)

# or
articles = session.query(Article).filter(or_(Article.title=='abc',Article.content=='abc'))
print(articles)