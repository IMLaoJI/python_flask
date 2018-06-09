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
    age = Column(Integer,default=0)
    gender = Column(Enum("male","female","secret"),default="male")


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(username='王武',age=17,gender='male')
# user2 = User(username='赵四',age=17,gender='male')
# user3 = User(username="张三",age=18,gender='female')
# user4 = User(username="张伟",age=19,gender='female')
# user5 = User(username="知了",age=20,gender='female')
#
# session.add_all([user1,user2,user3,user4,user5])
# session.commit()


# 每个年龄的人数
# from sqlalchemy.orm.query import Query
result = session.query(User.age,func.count(User.id)).group_by(User.age).having(User.age < 18).all()
print(result)
