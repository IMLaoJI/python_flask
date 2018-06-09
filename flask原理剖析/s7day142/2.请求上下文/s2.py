from flask.globals import _request_ctx_stack
from functools import partial

def _lookup_req_object(name):
    # name = request
    # top= ctx
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError('不存在')
    # return ctx.request
    return getattr(top, name)

class Foo(object):
    def __init__(self):
        self.xxx = 123
        self.ooo = 888

req = partial(_lookup_req_object,'xxx')
xxx = partial(_lookup_req_object,'ooo')

# 当前求刚进来时
_request_ctx_stack.push(Foo())

# 使用
# obj = _request_ctx_stack.top
# obj.xxx
v1 = req()
print(v1)
v2 = xxx()
print(v2)


# 请求终止，将local中的值移除
_request_ctx_stack.pop()

