# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午2:16
"""
from flask import Blueprint

from app.core import json_response

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
@json_response
def login():
    return ''
