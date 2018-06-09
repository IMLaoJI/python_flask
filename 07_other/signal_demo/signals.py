#encoding: utf-8

from blinker import Namespace
from datetime import datetime
from flask import request,g

namespace = Namespace()

login_signal = namespace.signal('login')

def login_log(sender):
    # 用户名，登录的时间，ip地址
    now = datetime.now()
    ip = request.remote_addr
    log_line = "{username}*{now}*{ip}".format(username=g.username,now=now,ip=ip)
    with open('login_log.txt','a') as fp:
        fp.write(log_line+"\n")

login_signal.connect(login_log)