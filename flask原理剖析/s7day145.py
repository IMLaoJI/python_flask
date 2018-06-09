s7day145

内容回顾：
	1.面向对象中的特殊方法
		
		
	2. metaclass
	
		__new__  真正创建对象
			- 单例
			- WTForms：当前对象/UnboundField对象
			- rest framework序列化：
					many=True
					many=False
				
		__init__ 对对象做初始化
		
	3. session源码流程：
		...
		
	4. wtforms流程：
		- 创建类，由metaclass创建类。
				  类：{
					 字段：UnBoundField(...)  ,听过计数器实现顺序
				  }
				  
		- 实例化
				对象：{
					字段：StringField(插件)
					字段：PasswordField(插件)
				}
		- 使用：
			对象.字段 
			for item in 对象：
				pass
		
			对象.validate()
				- 钩子函数
				- 每个字段.valid(钩子函数)
				
	5. SQLAlchemy
		类：
			Base = ...
			class Users(Base):
				.....
				
				
			引擎：连接字符串、连接池...
			引擎.Base.create_all()
		
		操作：
			引擎：连接字符串、连接池...
			
			连接 = 从连接池中获取连接
			
			
			连接.add(ORM对象)
			
			连接.commit()
			连接.close()
					  

今日内容：
	1. SQLAlchemy
	
	2. Flask-SQLAlchemy
	
	问题：
		- 什么是fabric？用于做什么？示例
		- 什么是ansible？用于做什么？示例
		- 什么是salstack？用于做什么？示例
		
		
内容详细：
	1. SQLAlchemy
		a. 创建表
			#!/usr/bin/env python
			# -*- coding:utf-8 -*-
			import datetime
			from sqlalchemy import create_engine
			from sqlalchemy.ext.declarative import declarative_base
			from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

			Base = declarative_base()


			class Users(Base):
				__tablename__ = 'users'

				id = Column(Integer, primary_key=True)
				name = Column(String(32), index=True, nullable=False)
				email = Column(String(32), unique=True)
				ctime = Column(DateTime, default=datetime.datetime.now) # 3期师兄
				extra = Column(Text, nullable=True)

				__table_args__ = (
					#UniqueConstraint('id', 'name', name='uix_id_name'),
					#Index('ix_id_name', 'name', 'email'),
				)
				问题：
					- 字符编码
					- 引擎 
					
			class Hobby(Base):
				__tablename__ = 'hobby'
				id = Column(Integer, primary_key=True)
				caption = Column(String(50), default='篮球')


			class Person(Base):
				__tablename__ = 'person'
				nid = Column(Integer, primary_key=True)
				name = Column(String(32), index=True, nullable=True)
				hobby_id = Column(Integer, ForeignKey("hobby.id"))

				
			######################
			class Server2Group(Base):
				__tablename__ = 'server2group'
				id = Column(Integer, primary_key=True, autoincrement=True)
				girl_id = Column(Integer, ForeignKey('girl.id'))
				boy_id = Column(Integer, ForeignKey('boy.id'))


			class Girl(Base):
				__tablename__ = 'girl'
				id = Column(Integer, primary_key=True)
				name = Column(String(64), unique=True, nullable=False)

			class Boy(Base):
				__tablename__ = 'boy'

				id = Column(Integer, primary_key=True, autoincrement=True)
				hostname = Column(String(64), unique=True, nullable=False)

	
		b. 操作表
			- 基本
				- 增删改查
			- 常用
				- 分组
				- 分页
				- 模糊。。。
				
			- relationship
			
			- 原生SQL
		
		
	2. Flask-SQLAlchemy(文件和目录的管理)
		- Flask和SQLAlchemy的管理者
	
	    - db = SQLAlchemy()
			- 包含配置
			- 包含ORM基类
			- 包含create_all
			- engine
			- 创建连接
				
		# 目录结构保存好
		
	3. pipreqs
	
		pip3 install pipreqs
		
		pipreqs ./
		
		
总结：
	1. SQLAlchemy操作
	
	2. Flask-SQLAlchemy操作(目录)
	
	3. 规范：pipreqs

作业：
	1. 表引擎+字符编码
	
	2. SQLAlchemy操作
	
	3. drop_all 
	
	4. 会议室预定
	
	5. 学习：
			- fabric
			- ansible
			- saltstack























		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		