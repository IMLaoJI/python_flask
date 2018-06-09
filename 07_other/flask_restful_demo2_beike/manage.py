#encoding: utf-8

from flask_script import Manager
from flask_restful_demo2 import app
from flask_migrate import MigrateCommand,Migrate
from exts import db
import models

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()