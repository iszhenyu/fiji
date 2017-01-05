# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/21 下午5:58
"""
import logging
import os
from logging.handlers import SMTPHandler, TimedRotatingFileHandler

from flask import Flask

from app.core import register_blueprints
from app.extensions import login_manager, db


def create_app(app_name, blueprint_package, blueprint_path, settings_override=None):
    """
    创建Flask应用
    :param app_name: 应用的名称
    :param blueprint_package: 蓝图所在包名
    :param blueprint_path:
    :param settings_override:
    :return:
    """
    app = Flask(app_name, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app.root_path = root
    # app.template_folder = 'public'
    # app.static_folder = 'public'

    _configure_logging(app)
    _configure_extensions(app)
    _configure_blueprints(app, blueprint_package, blueprint_path)

    return app


def _configure_logging(flask_instance):
    mail_enabled = flask_instance.config['MAIL_ENABLED']
    mail_handler = SMTPHandler(flask_instance.config['MAIL_SERVER'],
                               flask_instance.config['MAIL_DEFAULT_SENDER'],
                               flask_instance.config['MAIL_RECEIVER'],
                               'Application Error')

    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter('''
        Message type:       %(levelname)s
        Location:           %(pathname)s:%(lineno)d
        Module:             %(module)s
        Function:           %(funcName)s
        Time:               %(asctime)s

        Message:

        %(message)s
    '''))

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )

    # 配置log
    if flask_instance.debug or flask_instance.testing:
        warn_log = flask_instance.config['LOG_DEV']
    else:
        warn_log = flask_instance.config['LOG_PRODUCTION']
    if not warn_log.startswith('/'):
        warn_log = os.path.join(flask_instance.root_path, warn_log)

    file_handler = TimedRotatingFileHandler(warn_log, when='midnight', interval=1)
    file_handler.setFormatter(formatter)
    if flask_instance.debug or flask_instance.testing:
        file_handler.setLevel(logging.DEBUG)
    else:
        file_handler.setLevel(logging.INFO)

    loggers = [flask_instance.logger, logging.getLogger('pymongo')]
    for logger in loggers:
        logger.addHandler(file_handler)
        if mail_enabled:
            logger.addHandler(mail_handler)


def _configure_extensions(flask_instance):
    login_manager.init_app(flask_instance)
    db.init_app(flask_instance)


def _configure_blueprints(flask_instance, blueprint_package, blueprint_path):
    register_blueprints(flask_instance, blueprint_package, blueprint_path)
