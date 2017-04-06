# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 上午11:54
"""
from datetime import timedelta

DEBUG = True
SECRET_KEY = 'super-secret-key'

SQLALCHEMY_DATABASE_URI = 'mysql://root:3013689@localhost/fiji_new'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 30
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_ENABLED = False
MAIL_SERVER = '10.0.1.101'
MAIL_DEFAULT_SENDER = 'no-reply@17zuoye.com'
MAIL_RECEIVER = [
    'zhen.yu@17zuoye.com'
]

SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_PASSWORD_HASH = 'plaintext'
SECURITY_PASSWORD_SALT = 'password_salt'
SECURITY_REMEMBER_SALT = 'remember_salt'
SECURITY_RESET_SALT = 'reset_salt'
SECURITY_RESET_WITHIN = '5 days'
SECURITY_CONFIRM_WITHIN = '5 days'
SECURITY_SEND_REGISTER_EMAIL = False

CACHE_TYPE = 'simple'

LOG_NAME = 'fiji.log'

DEFAULT_PER_PAGE = 10

PERMANENT_SESSION_LIFETIME = timedelta(seconds=1800)