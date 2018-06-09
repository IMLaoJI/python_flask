s7day142 Flask 

内容回顾：
	1. 面向对象私有
		class Foo(object):

			def __init__(self):
				self.name = 'alex'
				self.__age = 18

			def get_age(self):
				return self.__age

		obj = Foo()
		# print(obj.name)
		# print(obj.get_age())
		# 强制获取私有字段
		print(obj._Foo__age)
		
	2. 谈谈Flask上下文管理
		- 与django相比是两种不同的实现方式。
			- django/tornado是通过传参数形式
			- flask是通过上下文管理
			两种都可以实现，只不过试下方式不一样。
			- 上下文管理：
				- threading.local/Local类，其中创建了一个字典{greelet做唯一标识：存数据} 保证数据隔离
				- 请求进来：
					- 请求相关所有数据封装到了RequestContext中。
					- 再讲RequestContext对象添加到Local中（通过LocalStack将对象添加到Local对象中）
				- 使用，调用request
					- 调用此类方法 request.method、print(request)、request+xxx 会执行LocalProxy中对应的方法
					- 函数
					- 通过LocalStack去Local中获取值。
				- 请求终止
					- 通过LocalStack的pop方法 Local中将值异常。

	3. DBUtils
		- 模式一：...
		- 模式二：...
		PS: SQLHelper
		
	
今日内容：
	1. 上下文
	
	2. 信号 
	
	3. session
	
	4. 会议室预定：表结构
	

内容详细：
	1. 上下文
		a. 请求上下文
			- request
			- session 
		b. 应用上下文
			
		
		请求流程：
				_request_ctx_stack.local = {
					
				}
				
				_app_ctx_stack.local = {
					
				}
		
		
			1. 请求到来 ，有人来访问
				# 将请求相关的数据environ封装到了RequestContext对象中
				# 再讲对象封装到local中（每个线程/每个协程独立空间存储）
				# ctx.app # 当前APP的名称
				# ctx.request # Request对象(封装请求相关东西)
				# ctx.session # 空
				_request_ctx_stack.local = {
					唯一标识：{
						"stack":[ctx, ]
					},
					唯一标识：{
						"stack":[ctx, ]
					},
				}
				
				
				# app_ctx = AppContext对象
				# app_ctx.app
				# app_ctx.g
					
				_app_ctx_stack.local = {
					唯一标识：{
						"stack":[app_ctx, ]
					},
					唯一标识：{
						"stack":[app_ctx, ]
					},
				}
			
			2. 使用 
					from flask import request,session,g,current_app
					
					print(request,session,g,current_app)
					
					都会执行相应LocalProxy对象的 __str__
					
					current_app = LocalProxy(_find_app)
						request = LocalProxy(partial(_lookup_req_object, 'request'))
						session = LocalProxy(partial(_lookup_req_object, 'session'))
						
						current_app = LocalProxy(_find_app)
						g = LocalProxy(partial(_lookup_app_object, 'g'))
					
			3. 终止，全部pop
	
			问题1：多线程是如何体现？
			问题2：flask的local中保存数据时，使用列表创建出来的栈。为什么用栈？
				   - 如果写web程序，web运行环境；栈中永远保存1条数据（可以不用栈）。
				   - 写脚本获取app信息时，可能存在app上下文嵌套关系。
						from flask import Flask,current_app,globals,_app_ctx_stack

						app1 = Flask('app01')
						app1.debug = False # 用户/密码/邮箱
						# app_ctx = AppContext(self):
						# app_ctx.app
						# app_ctx.g

						app2 = Flask('app02')
						app2.debug = True # 用户/密码/邮箱
						# app_ctx = AppContext(self):
						# app_ctx.app
						# app_ctx.g



						with app1.app_context():# __enter__方法 -> push -> app_ctx添加到_app_ctx_stack.local
							# {<greenlet.greenlet object at 0x00000000036E2340>: {'stack': [<flask.ctx.AppContext object at 0x00000000037CA438>]}}
							print(_app_ctx_stack._local.__storage__)
							print(current_app.config['DEBUG'])

							with app2.app_context():
								# {<greenlet.greenlet object at 0x00000000036E2340>: {'stack': [<flask.ctx.AppContext object at 0x00000000037CA438> ]}}
								print(_app_ctx_stack._local.__storage__)
								print(current_app.config['DEBUG'])

							print(current_app.config['DEBUG'])
	
	2. 多app应用
	
			from werkzeug.wsgi import DispatcherMiddleware
			from werkzeug.serving import run_simple
			from flask import Flask, current_app

			app1 = Flask('app01')

			app2 = Flask('app02')



			@app1.route('/index')
			def index():
				return "app01"


			@app2.route('/index2')
			def index2():
				return "app2"

			# http://www.oldboyedu.com/index
			# http://www.oldboyedu.com/sec/index2
			dm = DispatcherMiddleware(app1, {
				'/sec': app2,
			})

			if __name__ == "__main__":
				run_simple('localhost', 5000, dm)
			
			
			问题：Web访问多app应用时，上下文管理是如何实现？
			
	总结：
		1. threading.local (哪里还用到过threading.local: DBUtils )
		2. 上下文 
			- 请求 
				- request
				- session 
			- 应用
				- app 
				- g，每个请求周期都会创建一个用于在请求周期中传递值的一个容器。
		3. 多app应用 & 蓝图 
		
		4. 栈？
		
		5. 面向对象
			- 封装 
				class Foo:
					def __init__(self):
						self.age = 123
						self.nmame = 'ssdf'
	
	
				class Bar:
					def __init__(self):
						self.xx = 111
						
				
				
				class Base:
					def __init__(self):
						self.f = Foo()
						self.x = Bar()
			- 某个值+括号
				- 函数/方法
				- 类
				- 对象 
			
			- 特殊的双下划线方法：
				__new__
				__call__
				__str__
				__setattr__
				__setitem__
				__enter__
				__exit__
				__add__
				
				PS: Flask的LocalProxy中全部使用。
				
			- 强制调用私有字段
				- 派生类中无法调用基类私有字段
		6. 源码流程
			
			PS: 自定义栈
		
	3. 信号
		
		a. before_first_request
		b. 触发 request_started 信号
		c. before_request
		d. 模板渲染
			渲染前的信号 before_render_template.send(app, template=template, context=context)
				rv = template.render(context) # 模板渲染
			渲染后的信号 template_rendered.send(app, template=template, context=context)
		e. after_request
		f. session.save_session()
		g. 触发 request_finished信号
		
		如果上述过程出错：
			触发错误处理信号 got_request_exception.send(self, exception=e)
			
		h. 触发信号 request_tearing_down
				
		由信号引发的源码流程：找扩展点
				
					
	4. 会议预定表结构：
		
		用户表：
			ID     姓名 
			 1     放景洪
			 2     放景洪2
		
		会议室表：
			ID     名称
			1     马尔代夫
			2     塞班
			3     沙河
		
		时间段表：
			1      8:30 - 9:30
			2      9:30 - 10:30
			....
		
		预定表：
			用户     会议室         日期          时间段
			 1         1         2018-03-27         1
			 1         1         2018-03-28         1
			 1         2         2018-04-28         3
			 ...
			 联合唯一
			 
			
今日作业：
	1. 上下文管理（细节） + 博客
	2. 流程
	3. 会议室预定 （明天晚上交了）
		
	预习：
		session
		wtforms
		sqlalchemy
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	