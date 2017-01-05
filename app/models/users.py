# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/4 下午7:49
"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.core import JsonSerializer
from app.extensions import db


class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'username', 'email', 'mobile']


class User(UserJsonSerializer, UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(255), unique=True)
    mobile = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    registered_at = db.Column(db.DateTime())

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username
