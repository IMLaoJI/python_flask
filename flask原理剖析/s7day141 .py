s7day141 

内容回顾：
	1. 手写hello world
	2. Flask知识点
		- 配置文件
			- django中间件
			- 可扩展实例：短信、微信、邮件
		- 闪现
		- 路由系统:郑国栋
			- 装饰器
				- url
				- method
				- endpoint    url_for
			- 自定义路由
			- 作业：用户登录
				- 装饰器位置
				- endpoint重名？2中方式
		- 请求扩展：
			- 请求 
			- 错误处理
			- 模板函数
		- 蓝图 李俊毅
			- 目录实现多文件程序
			
		- 请求响应相关
			- 请求  周俊豪
			- 响应 
			
		- 中间件
		
		- 山下文
			- threading.local 
			- 自定义功能
				from greenlet import current... as get_ident
				
				class Local(object):
					
					def __init__(self):
						# self.storage =  {}
						object.__setattr__(...)
						
					def __setattr__(key,valu):
						pass
			
	3. 偏函数			
		import functools
		def func(a1):
			print(a1)
		new_func = functools.partial(func,666)
		new_func()
					
	4. 面向对象
		class Foo(object):

			def __init__(self,num):
				self.num = num

			def __add__(self, other):
				data = self.num + other.num
				return Foo(data)
			
		obj1 = Foo(11)
		obj2 = Foo(22)

		v = obj1 + obj2
		
		PS: 当把面向对象中的所有__函数__实现时，对象做任何操作时，都会执行其中对应的方法。
		
	5. 拼接列表中的值
		
		实例一：	
			v1 = [11,22,33]
			v2 = [44,55,66]

			new = chain(v1,v2)
			for item in new:
				print(item)
				
		实例二：
			from itertools import chain

			def f1(x):
				return x + 1

			func1_list = [f1,lambda x:x-1]

			def f2(x):
				return x + 10


			new_fun_list = chain([f2],func1_list)
			for func in new_fun_list:
				print(func)


今日内容：
	1. 上下文
	
	2. 数据库连接池：threading.local实现
	
	3. 信号
	
	
内容详细：
	1. 上下文 
		- threading.Local和Flask自定义Local对象
		- 请求到来
			- ctx = 封装RequestContext(request,session)
			- ctx放到Local中
		- 执行视图时
			- 导入request
			- print(request)   -->  LocalProxy对象的__str__
			- request.method   -->  LocalProxy对象的__getattr__
			- request + 1      -->  LocalProxy对象的__add__
				- 调用 _lookup_req_object函数：去local中将requestContext想获取到，再去requestContext中获取request或session
		- 请求结束
			- ctx.auto_pop()
			- ctx从local中移除。
	
	2. 数据库连接池：
		http://www.cnblogs.com/wupeiqi/articles/8184686.html
		
		前夕：
				Django：django ORM (pymysql/MySQLdb)
			Flask/其他：
					- 原生SQL
						- pymysql(2/3)
						- MySQLdb(2)
					- SQLAchemy（ORM） (pymysql/MySQLdb)
		
		
		原生SQL：
			1. 原生SQL 
				import pymysql
				CONN = pymysql.connect(host='127.0.0.1',
									   port=3306,
									   user='root',
									   password='123',
									   database='pooldb',
									   charset='utf8')
				
	
				cursor = CONN.cursor()
				cursor.execute('select * from tb1')
				result = cursor.fetchall()
				cursor.close()
				
				print(result)
				
			2. 问题 
			
			
			3. 解决：
				- 不能为每个用户创建一个链接。
				- 创建一定数量的连接池，如果有人来。
				
			4. 使用DBUtils模块：
				- 安装：如果安装到虚拟环境：需要先切换到虚拟
				- 使用：
					- 模式一：为每个线程创建连接。
					- 模式二：创建n个连接，多线程来时，去获取。
				
			5. 工作
				import pymysql
				from DBUtils.PooledDB import PooledDB
				POOL = PooledDB(
					creator=pymysql,  # 使用链接数据库的模块
					maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
					mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
					maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
					maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
					blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
					maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
					setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
					ping=0,
					# ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
					host='127.0.0.1',
					port=3306,
					user='root',
					password='123',
					database='pooldb',
					charset='utf8'
				)

				"""
				class SQLHelper(object):
					
					@staticmethod
					def fetch_one(sql,args):
						conn = POOL.connection()
						cursor = conn.cursor()
						cursor.execute(sql, args)
						result = cursor.fetchone()
						conn.close()
						return result

					@staticmethod
					def fetch_all(self,sql,args):
						conn = POOL.connection()
						cursor = conn.cursor()
						cursor.execute(sql, args)
						result = cursor.fetchone()
						conn.close()
						return result
					
				# 以后使用：
				result = SQLHelper.fetch_one('select * from xxx',[])
				print(result)
				"""
	
今日作业：
	1. 上下文源码流程（看图）
		- 2.5 个小时
		
	2. 找源码（1.5小时）：
		- before_first_request是如实现？
		- before_request是如实现？
		- after_request是如实现？
		实施：
			- 代码刚启动？
			- 请求到来时？chain
		
		
		
		找路由匹配（可选）
			
	3. 分组实现：会议室预定（Flask)
		- 设计表【必须】
		- 基于蓝图，基于before_request是如实现用的登录。【必须】
	
	早上早到10分钟：上节内容
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	