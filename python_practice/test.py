# -*- coding: utf-8 -*-
import contextlib
import datetime
import time
import operator
from urllib.parse import unquote
from itertools import zip_longest

# 测试用脚本

print(unquote("http://52.83.208.161:8001/api/v1/event_stats?date_stop=20210219&event_name=%5B%22__user_earnings_rmb%22%2C+%22__active%22%5D&date_start=20210219&from_cache=True&timeout=30&result_id=case-7two1n7fj"))


def student(*args, male, graduated):

    [print(a) for a in args]

    print("male: {}".format(male))
    print("graduated: {}".format(graduated))

student("Max","lala", male=True, graduated=False)
