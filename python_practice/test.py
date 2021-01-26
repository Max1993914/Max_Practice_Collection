# -*- coding: utf-8 -*-
import contextlib
import datetime
import time

a = datetime.datetime.fromtimestamp(9999999999.0)
print(a)

a_list = [1, 2, 3]
b_list = a_list[:]  # 完整复制一份
assert a_list == b_list and a_list is not b_list


class A(object):
    def __init__(self):
        self.__data = "good"  # private
        self._age = 10  # protected

a = A()
# a.__data   # 报错
print(a._A__data) # 可以正常获取
print(a._age)
