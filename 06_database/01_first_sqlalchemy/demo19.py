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
    city = Column(String(50),nullable=False)
    age =  Column(Integer,default=0)

    def __repr__(self):
        return "<User(username: %s)>" % self.username


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='李A',city="长沙",age=18)
# user2 = User(username='王B',city="长沙",age=18)
# user3 = User(username='赵C',city="北京",age=18)
# user4 = User(username='张D',city="长沙",age=20)
#
# session.add_all([user1,user2,user3,user4])
# session.commit()


# 婚恋
# 寻找和李A这个人在同一个城市，并且是同年龄的人
# user = session.query(User).filter(User.username=='李A').first()
# users = session.query(User).filter(User.city==user.city,User.age==user.age).all()
# print(users)

stmt = session.query(User.city.label("city"),User.age.label("age")).filter(User.username=='李A').subquery()
result = session.query(User).filter(User.city==stmt.c.city,User.age==stmt.c.age).all()
print(result)