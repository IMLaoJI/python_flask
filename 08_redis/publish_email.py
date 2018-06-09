#encoding: utf-8

from redis import Redis

cache = Redis(host='192.168.1.15',port=6379,password='zhiliao')

for x in range(3):
    cache.publish('email','xxx@qq.com')