
"""
需求：不用数据库连接池，显示数据库连接
"""
class SQLHelper(object):

    def open(self):
        pass

    def fetch(self,sql):
        pass

    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# obj = SQLHelper()
# obj.open()
# obj.fetch('select ....')
# obj.close()


with SQLHelper() as obj: # 自动调用类中的__enter__方法, obj就是__enter__返回值
    obj.fetch('xxxx')
    # 当执行完毕后，自动调用类 __exit__ 方法

# 以后如果遇到：