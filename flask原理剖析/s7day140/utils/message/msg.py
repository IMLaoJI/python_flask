from .base import Base

class Msg(Base):
    """
    发送短信提醒相关
    """

    def __init__(self):
        """
        短信相关数据初始化
        """
        self.username = 'asdf'
        self.pwd = 'asdf'

    def send(self, msg):
        pass