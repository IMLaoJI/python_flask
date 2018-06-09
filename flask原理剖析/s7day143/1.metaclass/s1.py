
class MyType(type):
    def __init__(self,*args,**kwargs):
        print('init')
        super(MyType,self).__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('call本质：调用类的__new__，再调用类的__init__')
        return super(MyType,self).__call__( *args, **kwargs)


class Foo(metaclass=MyType):
    pass

class Bar(Foo):
    pass

obj = Bar()