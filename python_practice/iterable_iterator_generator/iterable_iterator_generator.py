# -*- coding: utf-8 -*-
"""
可迭代对象（Iterable），迭代器（Iterator），生成器（Generator）。
"""
from collections import Iterable, Iterator, Generator

# ----------------------------------------------------------------------------------------------------
# 1. 可迭代对象：实现了__iter__()方法的对象就是可迭代对象。
# 常见的可迭代对象：
#   集合和序列（list, tuple, set, dict, str）
#   文件对象
#   正确实现了__iter__函数的对象（返回迭代器），即可以通过iter(obj)函数获取迭代器
# 注意，实现了__getitem__()的对象本身可以使用iter()方法返回迭代器，但其本身不是可迭代对象
# ----------------------------------------------------------------------------------------------------


class IterTest:

    def __init__(self):
        self.value = [20, 30, 40]

    def __iter__(self):
        return iter(self.value)


i1 = IterTest()
print(isinstance(i1, Iterable))  # i1是一个可迭代对象
print(isinstance(i1, Iterator))  # i1并不是一个迭代器
print(iter(i1))  # 返回一个list_iterator迭代器
for item in i1:
    print(item)
print("----------------------------------------------------------------------------------------------------------------")


class IterTest2:

    def __init__(self):
        self.value = [50, 60, 70]

    def __getitem__(self, item):
        return self.value[item]


i2 = IterTest2()
print(isinstance(i2, Iterable))  # False, i2 并不是可迭代对象
for item in i2:
    print(item)


print("----------------------------------------------------------------------------------------------------------------")
# ----------------------------------------------------------------------------------------------------
# 2. 迭代器：同时实现了__iter__()和__next__()方法的对象，就是迭代器
# 迭代器对象不仅可以在for循环中使用，并且可以通过内置的next()函数进行调用
# ----------------------------------------------------------------------------------------------------


class IteratorTest:

    def __init__(self):
        self.values = [3, 5, 7, 9, 11]
        self.start = 0
        self.end = len(self.values)

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            v = self.values[self.start]
            self.start += 1
            return v
        else:
            self.start = 0
            raise StopIteration()


i3 = IteratorTest()
print(isinstance(i3, Iterable))  # 是可迭代对象
print(isinstance(i3, Iterator))  # 也是一个迭代器
for i in i3:  # 可以使用for循环遍历
    print(i)


print(next(i3))  # 也可以使用next函数一个值一个值取
print(next(i3))


# Python中，for循环的本质其实就是不断地通过调用next()来实现的：
# 以下代码完全等价于for循环：
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break

print("----------------------------------------------------------------------------------------------------------------")


# ----------------------------------------------------------------------------------------------------
# 3. 生成器：生成器是一种特殊的迭代器
# 生成器有两种实现方式： 生成器表达式和生成器函数
# 生成器的好处：当列表非常庞大时，不需要消耗大量内存来保存它，而是改用生成器这种"惰性计算序列"，需要的时候出一个数，再出一个数...
# ----------------------------------------------------------------------------------------------------

# 生成器表达式
g1 = (x*2 for x in range(3))
print(isinstance(g1, Generator))  # 首先它是一个生成器
print(isinstance(g1, Iterator))  # 也是迭代器
print(isinstance(g1, Iterable))  # 也是可迭代对象
print(next(g1))
print(next(g1))
print(next(g1))
# print(next(g1))  # Stop Iteration

# 正确使用生成器的方式还是使用for循环,也不会报出StopIteration的错误
g1 = (x*2 for x in range(3))
for item in g1:
    print(item)

# 但是要注意，生成器同迭代器一样，遍历到最后就枯竭了，所以这一次遍历不会输出任何东西。
for item in g1:
    print(item)
print("----------------------------------------------------------------------------------------------------------------")


# 生成器函数（使用yield关键字）
def powpow():
    for i in range(3):
        yield i**2


g2 = powpow()
for item in g2:
    print(item)

print("----------------------------------------------------------------------------------------------------------------")


# 生成器应用实例，杨辉三角
def yanghui_triangle(max_line):
    result = [1]
    n = 0
    while n < max_line:
        yield result
        temp = [1]
        for i, item in enumerate(result):
            if i == 0: continue
            temp.append(item + result[i-1])
        temp.append(1)
        result = temp
        n += 1


tri = yanghui_triangle(10)
for item in tri:
    print(item)






