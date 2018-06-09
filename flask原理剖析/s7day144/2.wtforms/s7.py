
class F4(object):
    pass

class F3(F4):
    pass

class F2_5(object):
    pass

class F2(F2_5):
    pass

class F1(F2,F3):
    pass

print(F1.__mro__)