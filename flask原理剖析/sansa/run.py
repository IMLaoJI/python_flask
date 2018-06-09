#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
生成依赖文件：
    pipreqs ./

"""
from sansa import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
