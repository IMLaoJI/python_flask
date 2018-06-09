#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 在Python3中才有这个enum模块，在python2中没有
import enum
from datetime import datetime

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
    # create_time = Column(DateTime,default=datetime.now)
    # read_count = Column(Integer,default=11)
    title = Column(String(50),name='my_title',nullable=False)
    # telephone = Column(String(11),unique=True)
    update_time = Column(DateTime,onupdate=datetime.now,default=datetime.now)

Base.metadata.drop_all()
Base.metadata.create_all()

article1 = Article(title='abc')

session.add(article1)
session.commit()

# article = session.query(Article).first()
# article.title = '123'
# session.commit()