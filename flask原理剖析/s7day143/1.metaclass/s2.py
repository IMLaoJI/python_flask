

# Base = type('Base', (object,), {})




class MyType(type):
    def __init__(self, *args, **kwargs):
        super(MyType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('xxxx')
        return super(MyType, cls).__call__(*args, **kwargs)


# Base = MyType('Base', (object,), {})

# MyType('Base', (object,), {}) 是有MyType创建； metaclass=MyType
# 1. type可以创建类metaclass=type；MyType也可以创建类metaclass=MyType
# 2. Base = MyType('Base', (object,), {}) -->
# class Base(metaclass=MyType):
#     pass
# class Foo(Base):
#     pass

class Foo(MyType('Base', (object,), {})):
    pass
obj = Foo()