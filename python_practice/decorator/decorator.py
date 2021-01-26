# -*- coding: utf-8 -*-
import logging
import functools

"""
装饰器：

基本作用：本质上是一个Python函数，它可以让目标函数在不改变原有代码的情况下增加额外的功能。

使用场景：插入日志，缓存，校验权限，性能测试，事务处理等。

好处：增强代码的重复利用性和程序的可读性。
"""


# ----------------------------------------------------------------------------------------------
# 如果没有装饰器，假设我们想要给一个函数A增加一个额外的功能，可以把函数A对象作为参数传入另一个函数B，函数B处理完额外功能后再调用A即可。
# 但这样做的坏处是A的调用方式发生了改变：
# ----------------------------------------------------------------------------------------------
# 错误用法
def warn_log(func):
    logging.warning("this is test 1")
    func()


def foo():
    print("foo")


warn_log(foo)  # 改变了foo的执行方式，不推荐。


# ----------------------------------------------------------------------------------------------
# 正确的做法是使用装饰器:)
# ----------------------------------------------------------------------------------------------
def warn_log2(func):
    def wrapper(*args, **kwargs):
        logging.warning("this is test 2")
        return func(*args, **kwargs)

    return wrapper


@warn_log2
def foo2():
    print("foo2")


foo2()  # 直接调用foo2即可。这样不仅原封不动执行了foo2的功能，也同时增加warn_log2的功能。
# ----------------------------------------------------------------------------------------------
# 装饰器的执行顺序：
# 当把@语法糖挂在函数定义上时，就执行了如下语句：foo2 = warn_log2(foo2)。
# 也就是说，现在的foo2函数对象其实就是wrapper。
# 所以，调用foo2()也就是调用wrapper()。
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 装饰器威力加强版：带参数装饰器。
# 除了我们传入的函数之外，可以让装饰器接收额外的参数
# ----------------------------------------------------------------------------------------------
def warn_log3(is_test):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_test:
                logging.warning("this is test 3")
            else:
                logging.warning("this is not test!")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@warn_log3(False)
def foo3():
    print("foo3")


foo3()  # 执行，将False传入装饰器，得到"this is not test!"的结果
# ----------------------------------------------------------------------------------------------
# 装饰器的执行顺序：
# 当把@语法糖挂在函数定义上时，就执行了如下语句：foo3 = warn_log3(False)(foo3)。
# 首先先执行warn_log3(False)，返回decorator函数。然后decorator再如之前一样接收foo3，于是foo3指向wrapper函数。
# 所以，调用foo3()也就是调用wrapper()。
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# 使用装饰器时会产生一个问题：函数的__name__属性变了：从原来的名字变成了"wrapper"。
# 如果想要使用原来的名字，则需要借助一个工具：functools.wraps(func)，把它挂在wrapper函数上就万事大吉了。
# ----------------------------------------------------------------------------------------------
def warn_log4(is_test):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if is_test:
                logging.warning("this is test 4")
            else:
                logging.warning("this is definitely not test")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@warn_log4(True)
def foo4():
    print("foo4")


print(foo3.__name__)  # 返回foo3，错！
print(foo4.__name__)  # 返回foo4，对！


# ----------------------------------------------------------------------------------------------
# 类装饰器：使用类来构造一个装饰器，其本质是利用__init__函数和__call__函数。
# 挂载类装饰器和函数装饰器类似，foo5 = Logg(foo5)，此时foo5指向一个Logg对象。
# 当调用foo5()时，其实是调用的Logg对象的__call__方法。
# 我们会发现使用类作为装饰器有两个好处：1. 更简洁，嵌套更少。 2. 可以用到一些继承的特性。
# ----------------------------------------------------------------------------------------------
# 不带参数的类装饰器
class Logg(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        logging.warning("logg before")
        self._func(*args, **kwargs)
        logging.warning("logg after")


@Logg
def foo5():
    print("foo5")


foo5()


# ----------------------------------------------------------------------------------------------
# 带参数的类装饰器, __init__函数就不能接收函数了，而是接收参数并保存起来，然后在__call__函数中传入函数对象。
# foo6 = Logg2(True)(foo6),foo6此时指向wrapper。
# 再调用foo6(),其实就是调用wrapper()。
# ----------------------------------------------------------------------------------------------
class Logg2(object):
    def __init__(self, is_test):
        self._is_test = is_test

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self._is_test:
                logging.warning("this is logg2 test!")
            else:
                logging.warning("this is not test !!!!!!")
            return func(*args, **kwargs)

        return wrapper


@Logg2(True)
def foo6():
    print("foo6")


foo6()

# 装饰器装饰类方法（+self）
# todo: 改日再说：）
