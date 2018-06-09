#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sansa import create_app
from sansa import db

app = create_app()

with app.app_context():
    db.create_all()
