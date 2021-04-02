# -*- coding: utf-8 -*-
import contextlib
import datetime
import collections
import time
import operator
from urllib.parse import unquote
from itertools import zip_longest
import re

url = unquote("http://ap-dataservice.appcloudbox.net:8001/api/v1/event_stats?date_start=20201201&date_stop=20210203&timeout=30&result_id=case-7qpstr7d4n&event_name=topic-7f3fv60rv%26play_click&from_cache=True")
print(url)

d_date = datetime.datetime(2021, 1, 3)
d_date = d_date + datetime.timedelta(days=2)
print(d_date)


a = "    ddddeee    "
print(a)
b = a.lstrip()
print(b)
c = a.strip()
print(c)

def myAtoi():
    pattern = re.compile(r'^[\+\-]?\d+')
    result = pattern.match("102")
    print(int(result.group()))

myAtoi()


ddd = dict()
print(list(ddd.keys()))

