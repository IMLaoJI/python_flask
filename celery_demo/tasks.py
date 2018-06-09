#encoding: utf-8

# celery
# pip install celery
# 在windows操作系统上，还要安装另外一个东西：eventlet
# pip install eventlet

# task：任务
# broker（中间人）：存储任务的队列
# worker：真正执行任务的工作者
# backend：用来存储任务执行后的结果

from celery import Celery
import time

celery = Celery("tasks",broker="redis://127.0.0.1:6379/0",backend="redis://127.0.0.1:6379/0")

@celery.task
def send_mail():
    print('邮件开始发送....')
    time.sleep(5)
    print('邮件发送结束！')
