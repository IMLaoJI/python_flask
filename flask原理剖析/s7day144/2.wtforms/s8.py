class Foo(object):
    def __init__(self):
        self.values = {
            'n1':'alex',
            'n2':'oldboy',
        }
        for k,v in self.values.items():
            setattr(self,k,v)


obj = Foo()

print(obj.n1)
