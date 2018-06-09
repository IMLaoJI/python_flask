#encoding: utf-8

from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

# 判断是否连接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())

class Person(object):
    name = 'xx'
    age = 18
    country ='xx'

# Person类 -> 数据库中的一张表
# Person类中的属性  -> 数据库中一张表字段
# Person类的一个对象 -> 数据库中表的一条数据

# p = Person('xx',xx)
# p.save()
#
# create table person(name varchar(200),age int,country=xxx)