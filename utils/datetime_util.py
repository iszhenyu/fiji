# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 16/9/21 上午11:02
"""
from datetime import datetime

import pytz

import time

_local_tz = pytz.timezone('Asia/Shanghai')
_utc_tz = pytz.utc


def local_timezone():
    return _local_tz


def utc_timezone():
    return _utc_tz


def get_tzname(datetime_instance):
    return None if not datetime_instance else datetime_instance.tzname()


def to_utc_time(datetime_instance):
    if not datetime_instance:
        return datetime_instance
    if datetime_instance.tzinfo:
        tzname = get_tzname(datetime_instance)
        if tzname == _utc_tz.zone:
            return datetime_instance
        if tzname == _local_tz.zone:
            return datetime_instance.astimezone(_utc_tz)
    raise Exception('unrecognised timezone {}'.format(datetime_instance.tzinfo or 'None'))


def to_local_time(datetime_instance):
    if not datetime_instance:
        return datetime_instance
    if datetime_instance.tzinfo:
        tzname = get_tzname(datetime_instance)
        if tzname == _local_tz.zone:
            return datetime_instance
        if tzname == _utc_tz.zone:
            return datetime_instance.astimezone(_local_tz)
    raise Exception('unrecognised timezone {}'.format(datetime_instance.tzinfo or 'None'))


def utc_now():
    """返回utc当前时间"""
    return _utc_tz.localize(datetime.utcnow())


def local_now():
    """返回当前本地时间"""
    return _local_tz.localize(datetime.now())


def format_datetime(dt, template='%Y-%m-%d %H:%M:%S'):
    if not dt:
        return ''
    return dt.strftime(template)


def to_timestamp(dt):
    return time.mktime(dt.timetuple())
