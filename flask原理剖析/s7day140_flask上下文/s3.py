

"""
{
   1368:{}
}



"""
import threading
try:
    from greenlet import getcurrent as get_ident # 协程
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident # 线程


class Local(object):
    def __init__(self):
        self.storage = {}
        self.get_ident = get_ident

    def set(self,k,v):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            origin = {k:v}
        else:
            origin[k] = v
        self.storage[ident] = origin

    def get(self,k):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            return None
        return origin.get(k,None)

local_values = Local()


def task(num):
    local_values.set('name',num)
    import time
    time.sleep(1)
    print(local_values.get('name'), threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,),name='线程%s' % i)
    th.start()