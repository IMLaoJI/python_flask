import threading


#
# class Foo(object):
#     def __init__(self):
#         self.name = 0
#
# local_values = Foo()

local_values = threading.local()


def func(num):
    local_values.name = num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=func, args=(i,), name='线程%s' % i)
    th.start()