# -*- coding: utf-8 -*-
"""
描述符：
定义：一个类，只要它实现了__set__, __get__, __delete__中的一种或者多种，并且该类对象被其他类当作类属性，那么这个类就是一个描述符。

基本作用：一个描述符是一个有"绑定行为"的对象类属性。所谓"绑定行为"，即指属性在被访问、修改、删除时还做了额外的操作，比如判断数据类型，打印日志，做计算等。
        它可以作为别的类的类属性的一个"描述"。之所以使用描述符，是因为对于属性的描述不应该放在它所属的类中，而是应该放在另一个专门描述它的地方。
       （注意，是描述类属性，而不是对象属性！）

使用场景：1. 由于python是动态语言，python变量的类型需要等到赋值时才能控制。那么如何控制一个属性的类型呢？如果写在类属性的类中会显得很冗杂，这时可以
           把判断类型的逻辑写在另一个专门描述该属性的类中，这就是描述符。
        2. 当一个属性需要做一些额外处理的时候，比如计算，发日志等，都可以放在描述符里来做这些事情。
        3. 想设置不能被删除的时候，实现__delete__方法，并且抛出异常。

描述符的三个函数定义：
def __get__(self, instance, owner)：访问属性时会调用该方法
其中self指描述符的实例，instance指使用描述符的那个类的实例，onwer指使用描述符的那个类。
def __set__(self, instance, value)：修改属性时会调用该方法
def __delete__(self, instance)： 删除属性时会调用该方法
"""


# ------------------------------------------------------------------------------------------
# 首先举一个简单的例子，使用描述符去描述一个类的属性。
# ------------------------------------------------------------------------------------------
class CharacterDescriptor(object):

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, onwer):
        print("访问性格属性")
        return self.value

    def __set__(self, instance, value):
        print("设置性格属性")
        self.value = value


# 设置一个类去应用描述符
class Human(object):
    character = CharacterDescriptor("乐观的")


s1 = Human()
print(s1.character)  # 访问性格属性调用__get__方法，输出"乐观的"
s1.character = "悲观的"  # 设置性格属性，调用__set__方法
print(s1.character)  # 访问性格属性，输出"悲观的"
# ------------------------------------------------------------------------------------------
# 这里可以大致看出描述符的用处：我们专门创建一个类去描述另一个类的属性。这里，一个人有性格属性，
# 而我们把Human类中的类属性character指向描述符的一个对象时，当尝试获取这个属性时，会调用描述符中的__get__方法
# ------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------
# 下面展示一些比较实际的应用场景，比如我们要确保一个属性是string类型，如果传入别的类型会报错。如果不使用描述符：
# ------------------------------------------------------------------------------------------
class Student(object):

    name = None

    @classmethod
    def set_name(cls, val):
        if isinstance(val, str):
            cls.name = val
        else:
            raise TypeError("name must be string")

    @classmethod
    def get_name(cls):
        return cls.name


# 这样做的话也可以，但是会显得很冗余，更好的做法是把set，get的东西都写在描述符里
class NameType(object):
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        print("获取学生2姓名")
        return self.name

    def __set__(self, instance, value):
        print("设置学生2姓名")
        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError("name must be string")


# 测试类变得很纯净
class Student2(object):
    name = NameType()


s2 = Student2()
print(s2.name)  # None
s2.name = "王大壮"
print(s2.name)  # 王大壮
try:
    s2.name = 22  # 报错
except TypeError:
    print("name type is wrong")


