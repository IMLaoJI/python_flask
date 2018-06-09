#encoding: utf-8

from celery import Celery
import time

app = Celery("tasks",broker="redis://127.0.0.1:6379/0",backend="redis://127.0.0.1:6379/0")

app.conf.result_backend = "redis://localhost:6379/0"

@app.task
def send_mail():
    print('开始发送邮件...')
    time.sleep(2)
    print('邮件已经发送完成！')