"""
1. 什么意思？

# 类由type来创建
class Foo(metaclass=type)
# 继承Type
class Foo(type)

"""


class Foo(object):
    pass
obj = Foo()
# 对象是由类创建



# 一切皆对象,类由type创建
class Foo(object):
    pass

Foo = type('Foo',(object,),{})



# 一切皆对象,类由MyType创建
class MyType(type):
    pass
Foo = MyType('Foo',(object,),{})


class Foo(object,metaclass=MyType):
    pass



# 一切皆对象,类由MyType创建
class MyType(type):
    def __init__(self, *args, **kwargs):
        super(MyType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super(MyType, cls).__call__(*args, **kwargs)

Foo = MyType('Foo',(object,),{})


class Foo(object,metaclass=MyType):
    pass

Foo()