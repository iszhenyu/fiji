# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 16/9/21 下午2:46
"""
import random


def random_int(start=1000, end=9999):
    return random.randint(start, end)


def random_char(random_length=8):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    return _random(chars, random_length)


def random_str(random_length=8):
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    return _random(chars, random_length)


def _random(chars, random_length):
    result = ''
    length = len(chars) - 1
    for i in xrange(random_length):
        result += chars[random.randint(0, length)]
    return result
