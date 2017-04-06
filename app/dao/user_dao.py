# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/4/6 上午11:00
"""
from app.dao import BaseDao
from app.models.users import User


class UserDao(BaseDao):
    __model__ = User
