# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/14 下午4:54
"""
import decimal
from decimal import Decimal


decimal.getcontext().prec = 6


def divide(num1, num2, ndigits=2):
    r = Decimal(num1) / Decimal(num2)
    return round(r, ndigits)

