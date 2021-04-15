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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirror_tree(root):

    def recur(left, right):
        if not left and not right:
            return
        left, right = right, left
        if left:
            recur(left.left, left.right)
        if right:
            recur(right.left, right.right)

    recur(root.left, root.right)
    return root


a = TreeNode(10)
a.left = TreeNode(2)
a.right = TreeNode(8)


def test(left, right):
    print(id(left))
    print(id(right))
    left, right = right, left
    print(left == a.left)
    print(id(left))
    print(id(right))


test(a.left, a.right)
print(id(a), id(a.left), id(a.right))


class T(object):

    def __init__(self):
        self.left = None
        self.right = None
        self.value = [10, 20]

b = T()
b.left = T()
b.right = T()

print("dsfakljfdlksfkal")

def test2(left, right):
    print(id(left), id(right))
    left.value = [200, 400]
    temp = left
    right = left
    left = temp

test2(b.left, b.right)
print(b.left.value)

