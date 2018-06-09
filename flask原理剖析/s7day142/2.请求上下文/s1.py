from flask import Flask,request,session,g,current_app

app = Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def index():
    # request是 LocalProxy 的对象
    print(request)  # LocalProxy.__str__ --> str(LocalProxy._get_current_object) --> 调用偏函数 --> ctx.request
    request.method  # LocalProxy.__getattr__ -->
                                            # str(LocalProxy._get_current_object) --> 调用偏函数 --> ctx.request
                                            # getattr(self._get_current_object(), name)          --> ctx.request.method

    request.path   # ctx.request.path

    print(session) # LocalProxy.__str__ --> str(LocalProxy._get_current_object) --> 调用偏函数 --> ctx.session


    print(g) # 执行g对象的__str__
    return "index"


if __name__ == '__main__':
    # 1. app.__call__
    # 2. app.wsgi_app
    app.wsgi_app
    app.request_class
    app.run()