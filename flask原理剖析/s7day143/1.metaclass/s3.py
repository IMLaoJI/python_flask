class MyType(type):
    def __init__(self, *args, **kwargs):
        super(MyType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super(MyType, cls).__call__(*args, **kwargs)


def with_metaclass(base):
    return MyType('XX', (base,), {})


class Foo(with_metaclass(object)):
    pass

