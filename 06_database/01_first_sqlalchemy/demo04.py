#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 在Python3中才有这个enum模块，在python2中没有
import enum

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

class TagEnum(enum.Enum):
    python = "python"
    flask = "flask"
    django = "django"

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    # price = Column(Float)
    # is_delete = Column(Boolean)
    price = Column(DECIMAL(10,4))
    # 100000.0001
    # tag = Column(Enum(TagEnum))
    # create_time = Column(Date)
    # create_time = Column(DateTime)
    # create_time = Column(Time)
    # title = Column(String(50))
    # content = Column(Text)
    # content = Column(LONGTEXT)

# alembic
# flask-migrate
Base.metadata.drop_all()
Base.metadata.create_all()

from datetime import date
from datetime import datetime
from datetime import time

article = Article(price=100000.99999)
session.add(article)
session.commit()
