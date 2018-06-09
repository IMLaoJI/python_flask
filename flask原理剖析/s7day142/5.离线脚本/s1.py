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