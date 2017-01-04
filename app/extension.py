# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午6:20
"""
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'

db = SQLAlchemy()
