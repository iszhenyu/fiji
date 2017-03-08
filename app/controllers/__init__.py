# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午4:25
"""
from flask import abort
from flask import request
from flask import jsonify
from flask_login import current_user

from app import factory
from app.core import json_error, CustomJsonEncoder
from app.errors import FijiError, OrmError


def check_user_auth():
    """检查用户权限"""
    if request.path.startswith('/static') and request.method not in ('GET', 'POST'):
        return None
    if request.path.startswith('/api/auth'):
        return None
    if request.path.startswith('/api') and not current_user.is_authenticated:
        abort(401)


def create_app(settings_override=None):
    _app = factory.create_app(__name__, __name__, __path__, settings_override)
    _app.json_encoder = CustomJsonEncoder

    # 添加检查权限的请求预处理
    for blueprint in _app.blueprints.keys():
        if blueprint not in _app.before_request_funcs:
            _app.before_request_funcs[blueprint] = []
        _app.before_request_funcs[blueprint].append(check_user_auth)

    @_app.context_processor
    def inject_roles():
        pass

    @_app.before_request
    def before_request():
        pass

    # error handlers

    @_app.errorhandler(401)
    def page_not_found(e):
        response = json_error('unauthorized')
        response.status_code = 401
        return response

    @_app.errorhandler(403)
    def forbidden(e):
        response = json_error('forbidden')
        response.status_code = 403
        return response

    @_app.errorhandler(404)
    def page_not_found(e):
        response = json_error('page not found')
        response.status_code = 404
        return response

    @_app.errorhandler(500)
    def internal_server_error(e):
        _app.logger.exception('error 500: %s' % e)
        response = json_error('internal server error')
        response.status_code = 500
        return response

    @_app.errorhandler(FijiError)
    def custom_error_handler(e):
        if e.level in [FijiError.LEVEL_WARN, FijiError.LEVEL_ERROR]:
            if isinstance(e, OrmError):
                _app.logger.exception('%s %s' % (e.parent_error, e))
            else:
                _app.logger.exception('错误信息: %s %s' % (e.extras, e))
        response = jsonify(e.to_dict())
        response.status_code = e.status_code
        return response

    return _app
