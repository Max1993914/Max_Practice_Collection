# -*- coding: utf-8 -*-
import contextlib
import datetime
import collections
import time
import operator
from urllib.parse import unquote
from itertools import zip_longest
import re

url = unquote("http://test-ap-dataservice.appcloudbox.net:8081/api/v2/case_segment_analysis?report_id=6&metric=ltv_7&dimensions=['device_brand']")
print(url)


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

