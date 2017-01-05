# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午3:12
"""


class FijiException(Exception):
    default_status_code = 200

    LEVEL_DEBUG = 0
    LEVEL_INFO = 1
    LEVEL_WARN = 2
    LEVEL_ERROR = 3

    def __init__(self, message, error_code=None, extras=None, parent_error=None):
        self._message = message
        self._code = error_code
        self.extras = extras
        self.parent_error = parent_error
        self.level = FijiException.LEVEL_DEBUG

    @property
    def error_code(self):
        if not self._code:
            return FijiException.default_status_code
        return self._code

    def to_dict(self):
        rv = {
            'error_message': self._message,
            'error_code': self.error_code,
            'success': False
        }
        return rv


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
