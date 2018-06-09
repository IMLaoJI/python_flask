from .base import Base

class Email(Base):
    """
    发送邮件提醒相关
    """
    def __init__(self):
        """
        邮箱相关数据初始化
        """
        self.username = 'asdf'
        self.pwd = 'asdf'

    def send(self,msg):
        pass
