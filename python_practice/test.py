# -*- coding: utf-8 -*-
import contextlib
import datetime
import time
from urllib.parse import unquote
from itertools import zip_longest

# 测试用脚本

print(unquote("http://52.83.208.161:8001/api/v1/event_stats?date_stop=20210207&event_name=%5B%5B%22__active%22%5D%5D&date_start=20201209&from_cache=True&timeout=30&result_id=audience-7etjhsc3d"))


class Father(object):

    color = "red"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def scold(self):
        print("$%#^&$#@$!$@")


class Son(Father):

    def __init__(self, height, name, age):
        self.height = height
        super(Son, self).__init__(name, age)

    def cry(self):
        print("哇哇哇哇")


a = {"a": 1, "b": 2, "c": 3, "d": 4}
for k , v in a.items():
    if k == "b":
        a.pop(k)
    else:
        print(k)
