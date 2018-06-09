#encoding: utf-8

from redis import Redis

cache = Redis(host='192.168.1.15',port=6379,password='zhiliao')

# 1. 操作字符串
# cache.set('username','abcx')
# cache.delete('username')

# 2. 列表的操作
# cache.lpush('languages','java')
# cache.lpush('languages','python')
# cache.lpush('languages','php')
# print(cache.lrange('languages',0,-1))

# 3. 集合的操作
# cache.sadd('team','li')
# cache.sadd('team','huang')
# cache.sadd('team','zhang')
# print(cache.smembers('team'))

# 4. 哈希的操作
# cache.hset('website','baidu','www.baidu.com')
# cache.hset('website','google','www.google.com')
# print(cache.hgetall('website'))

# pip = cache.pipeline()
# pip.set('username','zhiliao')
# pip.set('password','1111')
# pip.execute()

# 发布与订阅功能
# 异步发送邮件的功能
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        if item['type'] == 'message':
            data = item['data']
            print(data)
            # 发送邮件