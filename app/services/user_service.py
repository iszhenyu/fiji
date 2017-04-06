# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午3:09
"""
from app.dao.user_dao import UserDao
from app.errors import ValidatorError
from app.services import BaseService


class UserService(BaseService):

    def __init__(self):
        super(UserService, self).__init__()
        self.user_dao = UserDao()

    def verify_user(self, mobile, password):
        user = self.user_dao.first(mobile=mobile)
        if user and user.verify_password(password):
            return user
        raise ValidatorError(u'手机号或密码错误')

    def register_user(self, mobile, password):
        user = self.user_dao.first(mobile=mobile)
        if user:
            raise ValidatorError(u'手机号已经注册,请直接登录')
        user = self.user_dao.new_instance(mobile=mobile, password=password)
        return self.user_dao.save(user)
