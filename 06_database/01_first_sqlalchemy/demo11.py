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


article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer,ForeignKey("article.id"),primary_key=True),
    Column("tag_id",Integer,ForeignKey("tag.id"),primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)

    # tags = relationship("Tag",backref="articles",secondary=article_tag)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    articles = relationship("Article",backref="tags",secondary=article_tag)

    def __repr__(self):
        return "<Tag(name:%s)>" % self.name

# 1. 先把两个需要做多对多的模型定义出来
# 2. 使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”。
# 3. 在两个需要做多对多的模型中随便选择一个模型，定义一个relationship属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个secondary=中间表。

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title="article1")
# article2 = Article(title="article2")
#
# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
#
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
# session.add(article1)
# session.add(article2)
#
# session.commit()


# article = session.query(Article).first()
# print(article.tags)

tag = session.query(Tag).first()
print(tag.articles)