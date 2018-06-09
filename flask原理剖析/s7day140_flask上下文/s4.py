class Foo(object):

    def __init__(self):
        object.__setattr__(self, 'storage', {})
        # self.storage = {}

    def __setattr__(self, key, value):
        self.storage = {'k1':'v1'}
        print(key,value)

    def __getattr__(self, item):
        print(item)
        return 'df'


obj = Foo()

# obj.x = 123
# 对象.xx

