class Foo(object):

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        """
        用于生成对象
        :param args:
        :param kwargs:
        :return:
        """

        return super(Foo,cls).__new__(cls, *args, **kwargs)
        # return "666"


obj = Foo()
print(obj)