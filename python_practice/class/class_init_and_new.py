# -*- coding: utf-8 -*-

"""
class 中的__init__方法和__new__方法
区别：在创建类的实例对象时，__new__方法用于创建一个对象，而__init__方法用于初始化对象
"""


class Test(object):

    def __new__(cls, *args, **kwargs):
        print("new")
        return super(Test, cls).__new__(cls)  # 注意，object.__new__()只接收一个参数

    def __init__(self, name, nick_name):
        self.name = name
        self.nick_name = nick_name
        print("init")


t1 = Test("Max", "gogo")  # 先输出new，后输出init

# 可以看出，当执行Test("Max", "gogo")时，首先执行__new__，它会将参数传递给父类new方法，最终返回一个对象，并作为__init__的第一个参数。
# 然后再次调用__init__方法，此时将"Max"传入对象，对对象t1进行初始化。
# __init__是初始化操作，当对象创建完毕后，它可以初始化对象，并且做一些额外操作。它属于实例级别的对象。
# __new__是构造类实例的方法，是类级别的方法。
print("-------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------
# 关于__new__和__init__的注意事项：
# 1. __new__必须要有返回值；__init__可以没有
# 2. __new__必须接收至少一个参数cls，表示当前类
# 3. 如果__new__返回的是一个已经存在的实例（可以是别的类的实例），则不会执行__init__方法
# ------------------------------------------------------------------------------------------
class Test2(object):

    def __new__(cls, *args, **kwargs):
        print("new2")
        return t1

    def __init__(self):
        print("init2")


t2 = Test2()  # 不执行__init__方法


# ------------------------------------------------------------------------------------------
# __new__函数的用法1：当类继承自一些不可变类型时，提供一定的自定义功能的能力。或者用于实现自定义的metaclass
# ------------------------------------------------------------------------------------------
class MyInt(int):

    def __new__(cls, num):
        return super(MyInt, cls).__new__(cls, abs(num))  # int重写了__new__()方法，所以可以接收不止一个参数


a = MyInt(-20)
print(a)  # 返回-20的绝对值20

print("-------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------
# __new__函数的用法2：单例设计模式
# 单例是一种设计模式，应用该模式的类只会生成一个实例。
# 单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：如果实例不存在，会创建一个实例；如果已存在就会返回这个实例。
# 举个例子来说，比如开发一款游戏软件，游戏中需要有“场景管理器”这样一种东西，用来管理游戏场景的切换、资源载入、网络连接等等任务。
# 这个管理器需要有多种方法和属性，在代码中很多地方会被调用，且被调用的必须是同一个管理器，否则既容易产生冲突，也会浪费资源。
# 这种情况下，单例模式就是一个很好的实现方法。
# ------------------------------------------------------------------------------------------
class Single(object):

    def __new__(cls):
        if not hasattr(cls, "my_instance"):
            cls.my_instance = super(Single, cls).__new__(cls)
        return cls.my_instance


o1 = Single()
o2 = Single()
o1.name = "Mama"
print(o1.name, o2.name)  # name相同
print(o1 is o2)  # True
