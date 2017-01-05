# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午6:20
"""
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def unauthorized_handler():
    abort(401)


def user_loader():
    pass


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.unauthorized_handler(unauthorized_handler)
login_manager.user_loader(user_loader)

db = SQLAlchemy()



