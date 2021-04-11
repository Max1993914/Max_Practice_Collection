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


def uniquePaths(m: int, n: int) -> int:
    result_sum = 0

    def back_trace(index_m, index_n):
        nonlocal result_sum
        if index_m == m - 1 and index_n == n - 1:
            result_sum += 1
            return
        elif index_m > m - 1 or index_n > n - 1:
            return

        back_trace(index_m + 1, index_n)
        back_trace(index_m, index_n + 1)

    back_trace(0, 0)
    return result_sum


a = 4  # 100
b = 2  # 010
print(a ^ b)