#encoding: utf-8

from flask_script import Manager
from zhiliao import app
from exts import db
from flask_migrate import Migrate,MigrateCommand
# 需要把映射到数据库中的模型导入到manage.py文件中
from models import User

manager = Manager(app)

# 用来绑定app和db到flask_migrate的
Migrate(app,db)
# 添加Migrate的所有子命令到db下
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()