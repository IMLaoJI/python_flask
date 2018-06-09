#encoding: utf-8

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

# create table person(id int primary key autoincrement,name varchar(50),age int)

# 1. 创建一个ORM模型，这个ORM模型必须继承自sqlalchemy给我们提供好的基类
class Person(Base):
    __tablename__ = 'person'
    # 2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。这些属性必须是sqlalchemy给我们提供好的数据类型。
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))
# 3. 将创建好的ORM模型，映射到数据库中。
Base.metadata.create_all()