# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午5:50
"""
from app.controllers import create_app

app = create_app()


if __name__ == '__main__':
    app.run()
