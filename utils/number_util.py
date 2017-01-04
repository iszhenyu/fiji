# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/12/14 下午4:54
"""
import decimal
from decimal import Decimal


decimal.getcontext().prec = 6


def divide(num1, num2):
    r = Decimal(num1) / Decimal(num2)
    return float(r.quantize(Decimal('.01'), decimal.ROUND_UP))


def average(*args):
    """
    平均值,保存两位小数
    :param args:
    :return:
    """
    total = Decimal('0')
    for item in args:
        total += Decimal(item)
    ave = total / len(args)
    return float(ave.quantize(Decimal('.01'), decimal.ROUND_UP))