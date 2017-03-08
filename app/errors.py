# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午3:12
"""


class FijiError(Exception):
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
        self.level = FijiError.LEVEL_DEBUG

    @property
    def error_code(self):
        if not self._code:
            return FijiError.default_status_code
        return self._code

    def to_dict(self):
        rv = {
            'error_message': self._message,
            'error_code': self.error_code,
            'success': False
        }
        return rv


class IllegalParameterError(FijiError):
    def __init__(self, message, extras=None):
        super(IllegalParameterError, self).__init__(message=message, extras=extras)
        self.level = FijiError.LEVEL_INFO


class ValidatorError(FijiError):
    def __init__(self, message, extras=None):
        super(ValidatorError, self).__init__(message=message, extras=extras)
        self.level = FijiError.LEVEL_INFO


class FormError(FijiError):
    def __init__(self, form):
        message = form.get_first_validate_error()
        super(FormError, self).__init__(message, extras=form.data)
        self.level = FijiError.LEVEL_INFO


class OrmError(FijiError):
    def __init__(self, message, status_code=None, extras=None, parent_error=None):
        super(OrmError, self).__init__(message, status_code, extras, parent_error)
        self.level = FijiError.LEVEL_ERROR
