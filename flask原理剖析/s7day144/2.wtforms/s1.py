class Foo(object):

    def __init__(self,name):
        self.name = name


obj = Foo('xx')

for item in obj:
    print(item)
