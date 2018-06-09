#encoding: utf-8

from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base


DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'alembic_demo'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    country = Column(String(50))

# ORM -> 迁移脚本 -> 映射到数据库中