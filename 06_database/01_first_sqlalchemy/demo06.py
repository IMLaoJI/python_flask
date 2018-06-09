#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func
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

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()


# for x in range(6):
#     article = Article(title='title%s'%x,price=random.randint(50,100))
#     session.add(article)
# session.commit()

# 模型对象
# articles = session.query(Article).all()
# print(articles)

# 模型中的属性
# articles = session.query(Article.title,Article.price).all()
# print(articles)

# 聚合函数
# result = session.query(func.count(Article.id)).first()
# print(result)
# result = session.query(func.avg(Article.price)).first()
# print(result)
# result = session.query(func.max(Article.price)).first()
# print(result)
# result = session.query(func.min(Article.price)).first()
# print(result)
# result = session.query(func.sum(Article.price)).first()
# print(result)
print(func.sum(Article.price))
# select sum(price) from article