# -*- coding: utf-8 -*-
"""
@author: xiaoz
@time: 2016/11/14 下午12:16
"""


def get_values_from_map(any_map=None, keys=None):
    if not any_map:
        return []
    if not keys:
        return any_map.values()
    result = []
    for key, val in any_map.items():
        if key in keys:
            result.append(val)
    return result


def equals_list(list1, list2):
    """
    判断两个数组是否包含同样的元素
    都是空数组也返回False
    :param list1:
    :param list2:
    :return:
    """
    if list1 and not list2:
        return False
    if not list1 and list2:
        return False
    if not list1 and not list2:
        return False
    if len(list1) != len(list2):
        return False
    for item in list1:
        if item not in list2:
            return False
    return True


def list_except_list(list1, list2):
    """
    两个list相减
    :param list1:
    :param list2:
    :return:
    """
    if not list1:
        return []
    if list1 and not list2:
        return list1
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    return result


def divide_list_equally(any_list, divider):
    """
    将一个list平均分成几等份
    :param any_list:
    :param divider: 份数
    :return:
    """
    if not any_list:
        return []
    divider = int(divider)
    if divider == 0 or divider == 1 or len(any_list) < divider:
        return any_list
    list_len = len(any_list)
    item_len = 1
    while (item_len * divider) < list_len:
        item_len += 1
    spare_count = (item_len * divider) - list_len
    full_count = divider - spare_count
    result = []
    for i in xrange(0, spare_count):
        result.append(any_list[i * (item_len - 1): (i + 1) * (item_len - 1)])
    spare_total = spare_count * (item_len - 1)
    for j in xrange(0, full_count):
        result.append(any_list[j * item_len + spare_total: (j + 1) * item_len + spare_total])
    return result


def rotate_list(any_list, rotate_num):
    """
    将list中的元素进行轮转
    :param any_list:
    :param rotate_num:
    :return:
    """
    if not any_list or len(any_list) == 1:
        return any_list
    list_len = len(any_list)
    rotate_num = int(rotate_num)
    if rotate_num == 0:
        return any_list
    real_rotate_num = (rotate_num % list_len) if rotate_num > list_len else rotate_num
    return any_list[real_rotate_num:] + any_list[0: real_rotate_num]
