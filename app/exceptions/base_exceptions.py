# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午6:40

程序的基本异常
"""
from app.exceptions import FijiException


class IllegalParameterException(FijiException):
    def __init__(self, message, extras=None):
        super(IllegalParameterException, self).__init__(message=message, extras=extras)
        self.level = FijiException.LEVEL_INFO


class FormException(FijiException):
    def __init__(self, form):
        message = form.get_first_validate_error()
        super(FormException, self).__init__(message, extras=form.data)
        self.level = FijiException.LEVEL_INFO


class OrmException(FijiException):
    def __init__(self, message, status_code=None, extras=None, parent_error=None):
        super(OrmException, self).__init__(message, status_code, extras, parent_error)
        self.level = FijiException.LEVEL_ERROR

