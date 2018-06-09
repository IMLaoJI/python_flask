
class Foo(object):

    def __init__(self):
        self.name = 'alex'
        self.__age = 18

    def get_age(self):
        return self.__age

obj = Foo()
# print(obj.name)
# print(obj.get_age())
# 强制获取私有字段
print(obj._Foo__age)