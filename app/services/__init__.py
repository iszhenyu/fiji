# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2017/1/5 下午2:17
"""
import threading

service_lock = threading.Lock()


class BaseService(object):

    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                service_lock.acquire()
                if not cls.__instance:
                    cls.__instance = super(BaseService, cls).__new__(cls, *args, **kwargs)
            finally:
                service_lock.release()
        return cls.__instance

