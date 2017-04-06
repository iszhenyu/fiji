# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午5:58
"""
import importlib
import pkgutil
from functools import wraps

from flask import Blueprint
from flask import abort
from flask import current_app
from flask import jsonify
from flask import make_response
from flask import request
from flask_login import current_user
from flask.json import dumps, JSONEncoder


def register_blueprints(app, package_name, package_path):
    """
    自动注册蓝图
    :param app:
    :param package_name:
    :param package_path:
    :return:
    """
    result_value = []
    for importer, name, ispkg in pkgutil.iter_modules(package_path):
        module = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(module):
            item = getattr(module, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            result_value.append(item)
    return result_value


class CustomJsonEncoder(JSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv


def role_required(role):
    """
    角色装饰器
    :param role:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            if not current_user.can(role):
                abort(403)
            return func(*args, **kwargs)

        return decorated_func
    return decorator


def json_response(func):
    """
    controller返回json的装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_code = 200
        result_value = func(*args, **kwargs)
        if isinstance(result_value, tuple):
            result_code = result_value[1]
            result_value = result_value[0]
        # if isinstance(result_value, Pagination):
        #     return _generate_page_result(result_value, result_code, **kwargs)
        return _output_response(_output_json(result_value), result_code)
    return wrapper


def _generate_page_result(pagination, result_code, **values):
    values['_external'] = True
    headers = {
        'Pagination-Total-Count': pagination.total,
        'Pagination-Total-Pages': pagination.pages,
        'Pagination-Cur-Page': pagination.page,
        'Pagination-Per-Page': pagination.per_page,
    }
    page_data = {
        'items': pagination.items,
        'total_count': pagination.total,
        'total_page': pagination.pages,
        'page': pagination.page,
        'page_size': pagination.per_page
    }
    json = _output_json(page_data)
    return _output_response(json, result_code, headers)


def _output_json(data):
    settings = current_app.config.get('RESTFUL_JSON', {})
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', True)
    settings.setdefault('separators', (',', ':'))

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps({'data': data, 'success': True}, **settings) + "\n"
    return dumped


def _output_response(json_data, code=200, headers=None):
    resp = make_response(json_data, code)
    resp.headers['Content-Type'] = 'application/json'
    resp.headers.extend(headers or {})
    return resp


def json_error(msg=''):
    """
    用于直接返回错误的json数据
    :param msg:
    :return:
    """
    return jsonify(success=False, error_message=msg)


def json_ok(data=None):
    """
    用于直接返回成功的json数据
    :param data:
    :return:
    """
    return jsonify(success=True, data=data)


def post_param(key, default_val=None):
    """
    从post请求中获取数据,屏蔽掉form和json的差异
    :param key:
    :param default_val:
    :return:
    """
    if request.form:
        return request.form.get(key, default_val)
    elif request.json:
        return request.json.get(key, default_val)
    else:
        return default_val


def post_int_param(key, default_val=None):
    """
    从post请求中获取int类型数据
    :param key:
    :param default_val:
    :return:
    """
    val = post_param(key, default_val)
    try:
        return int(val)
    except ValueError:
        return default_val


def get_param(key, default_val=None):
    """
    从get中获取参数
    :param key:
    :param default_val:
    :return:
    """
    return request.args.get(key, default_val)


def get_int_param(key, default_val=None):
    """
    从get中获取int类型参数
    :param key:
    :param default_val:
    :return:
    """
    val = get_param(key, default_val)
    try:
        return int(val)
    except ValueError:
        return default_val
