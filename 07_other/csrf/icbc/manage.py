#coding: utf8

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
import models
from exts import db
from icbc import app

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()