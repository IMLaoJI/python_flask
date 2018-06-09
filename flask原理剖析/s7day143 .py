s7day143 
内容回顾：
	1. Flask
		- 配置文件
		- 路由
		- 请求相关&响应
		- cookie&session
		- 模板jinja2
		- 扩展
		- 闪现
		- 蓝图
		- 中间件
	2. 上下文管理
		- threading.local
		
		- 请求上下文：RequstContext
			- request
			- session 
		- 应用上下文：AppContext
			- app(current_app)
			- g
		
		- 实现细节：
			- RequstContext（AppContext）对象通过LocalStack添加到Local中。
			- 导入request（session、current_app、g）是LocalProxy对象 -> 通过偏函数 -> LocalStack -> Local 
			- RequstContext的auto_pop  ->   LocalStack.pop  -> Local中移除
			PS：永远两个Local对象。
			
		- 多app应用
		
		- 为什么用栈？
		
		
		- 零碎：
			- LocalProxy类
			- 偏函数
			- chain
			
	3. 信号 （请求流程）
	
	4. MetaClass
		- MetaClass作用：用来指定当前类由谁来创建（默认type创建）。
		- 使用metaclass
			class Foo(metaclass=type):
				pass 
			
			class Foo(object):
				__metaclass__ = type
		- 类继承
			
			class MyType(type):
				def __init__(self,*args,**kwargs):
					print('init')
					super(MyType,self).__init__(*args,**kwargs)

				def __call__(self, *args, **kwargs):
					print('call本质：调用类的__new__，再调用类的__init__')
					return super(MyType,self).__call__( *args, **kwargs)


			class Foo(metaclass=MyType):
				pass

			class Bar(Foo):
				pass

			obj = Bar()
		- 问题：
			1. 什么意思？
				# 类由type来创建
				class Foo(metaclass=type)
				# 继承Type
				class Foo(type)
			2. Flask多线程：服务端开多线程
				
			
			
今日内容：
	1. flask-session
	2. wtforms
	3. SQLAchemy
	
	
内容详细：
	1. flask-session
		- Flask中的session处理机制（内置：将session保存在加密cookie中实现）
			
		
		
		
		
		
			- 请求刚到来：获取随机字符串，存在则去“数据库”中获取原来的个人数据，否则创建一个空容器。 --> 内存：对象（随机字符串，{放置数据的容器}）
				# 1. obj = 创建SecureCookieSessionInterface()
				# 2. obj = open_session(self.request) = SecureCookieSession()
				# self.session = SecureCookieSession()对象。 
				self.session = self.app.open_session(self.request)
			
			
			- 视图：操作内存中 对象（随机字符串，{放置数据的容器}）
			- 响应：内存对象（随机字符串，{放置数据的容器}）
					- 将数据保存到“数据库”
					- 把随机字符串写在用户cookie中。
					
				
		- 自定义 
			请求刚到来：
				# 创建特殊字典，并添加到Local中。
				# 调用关系：
				#	self.session_interface.open_session(self, request)
				# 	由于默认app中的session_interface=SecureCookieSessionInterface()
				#		SecureCookieSessionInterface().open_session(self, request)
				# 	由于默认app中的session_interface=MySessionInterFace()
				#		MySessionInterFace().open_session(self, request)
				self.session = self.app.open_session(self.request)
			
			调用：
				session -> LocalProxy -> 偏函数 -> LocalStack -> Local
			
			请求终止：
				# 	由于默认app中的session_interface=SecureCookieSessionInterface()
				#		SecureCookieSessionInterface().save_session(self, app, session, response)
				# 	由于默认app中的session_interface=MySessionInterFace()
				#		MySessionInterFace().save_session(self, app, session, response)
			
		- flask-session组件 
			- 使用：
				from flask import Flask,session
				from flask_session import RedisSessionInterface

				app = Flask(__name__)
				app.secret_key = 'suijksdfsd'
				
				# 方式一
				from redis import Redis
				conn = Redis()
				app.session_interface = RedisSessionInterface(conn,key_prefix='__',use_signer=False)
				
				# 方式二
				from redis import Redis
				from flask.ext.session import Session
				app.config['SESSION_TYPE'] = 'redis'
				app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
				Session(app)


				@app.route('/')
				def index():
					session['xxx'] = 123
					return 'Index'


				if __name__ == '__main__':

					app.run()
	
			- 源码：
				- 流程
				
			PS: 
				问题：设置cookie时，如何设定关闭浏览器则cookie失效。
					  response.set_cookie('k','v',exipre=None)
	
		
		总结：
			1. 内置原理 
			2. 如何进行自定义
			3. flask-session组件使用和原理
		
	2. wtforms
		安装：pip3 install wtforms 
	
		- 使用
			- 登录
			- 注册 
		- 如何实现？
			源码流程：
				1. 解释：metaclass
				2. 实例：form = LoginForm()
				3. 验证：form.validate()
		
作业：
	1. flask-session/wtforms => 会议室预定
	2. wtforms的源码流程
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	