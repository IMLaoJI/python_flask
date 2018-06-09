class Foo(object):
    AGE = 123
    def __init__(self,na):
        self.name = na


print(Foo.__dict__)
print(dir(Foo))

# obj = Foo('小月月')
# print(obj.__dict__)

