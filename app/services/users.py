# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午3:09
"""
from app.exceptions import ValidatorException
from app.models.users import User
from app.services import Service


class UserService(Service):
    __model__ = User

    def verify_user(self, mobile, password):
        user = self.first(mobile=mobile)
        if user and user.verify_password(password):
            return user
        raise ValidatorException(u'手机号或密码错误')

    def register_user(self, mobile, password):
        user = self.first(mobile=mobile)
        if user:
            raise ValidatorException(u'手机号已经注册,请直接登录')
        user = self.new_instance(mobile=mobile, password=password)
        return self.save(user)
