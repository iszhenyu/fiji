# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午3:09
"""
from app.models.users import User
from app.services import Service


class UserService(Service):
    __model__ = User
