# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午5:50
"""
import os

from app.controllers import create_app

app = create_app()


if __name__ == '__main__':
    # c = os.path.abspath(__file__)
    # print c
    # p = os.path.dirname(c)
    # print os.path.dirname(p)
    app.run()