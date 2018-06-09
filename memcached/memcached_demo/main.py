#encoding: utf-8

import memcache

# 在连接之前，一定要切记先启动memcached
mc = memcache.Client(["127.0.0.1:11211","192.168.0.102:11211"],debug=True)

# mc.set('username','abc',time=120)
# mc.set_multi({'title':'钢铁是怎样练成的','content':'hell world'},time=120)

# username = mc.get('username')
# print(username)
#
# mc.delete('username')
#
# username = mc.get('username')
# print(username)

# mc.incr('age',delta=10)
#
# age = mc.get('age')
# print(age)

# mc.decr('age',delta=10)
# age = mc.get('age')
# print(age)

mc.set_multi({'username':'zhiliao','age':18,'height':180,'weight':180,'country':'china'})