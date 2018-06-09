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
DATABASE = 'second_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    sno = Column(String(10),unique=True,nullable=False)
    name = Column(String(50),nullable=False)
    age = Column(Integer,nullable=False)
    sex = Column(Enum("male","female","secret"),default="male")

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer,primary_key=True,autoincrement=True)
    tno = Column(String(10),unique=True,nullable=False)
    name = Column(String(50),nullable=False)

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True,autoincrement=True)
    cno = Column(String(10),unique=True,nullable=False)
    name = Column(String(50),nullable=False)
    teacher_id = Column(Integer,ForeignKey("teacher.id"))

    teacher = relationship("Teacher",backref="courses")

class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer,primary_key=True,autoincrement=True)
    student_id = Column(Integer,ForeignKey("student.id"))
    course_id = Column(Integer,ForeignKey("course.id"))
    point = Column(Float,default=0)

    student = relationship("Student",backref="scores")
    course = relationship("Course",backref="scores")

Base.metadata.drop_all()
Base.metadata.create_all()


genders = ["male","female","secret"]
random.shuffle(genders)
students = []
for x in range(5):
    name = 'student %s' % x
    sno = '00%s' % x
    age = random.randint(18,30)
    sex = random.choice(genders)
    student = Student(name=name,sex=sex,sno=sno)
    session.add(student)
    students.append(student)

from sqlalchemy.orm.query import Query
teachers = []
for x in range(3):
    pass


