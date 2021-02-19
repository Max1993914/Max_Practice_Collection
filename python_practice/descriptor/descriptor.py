# -*- coding: utf-8 -*-
"""
描述符：
定义：一个类，只要它实现了__set__, __get__, __delete__中的一种或者多种，并且该类对象被其他类当作类属性（类属性包括函数）时，那么这个类就是一个描述符。
     其中，只定义了__get__的描述符为非数据描述符；定义了__set__或__delete__的描述符为数据描述符。

数据描述符与非数据描述符的区别：如果实例的字典与数据描述符有同名项，则优先选择数据描述符；反之，如果实例的字典与非数据描述符有同名项，则优先选择实例字典。
                          为了使数据描述器成为只读的，应该同时定义__set__和__get__，并且在__set__方法中raise AttributeError。

基本作用：一个描述符是一个有"绑定行为"的对象。所谓"绑定行为"，即指属性在被访问、修改、删除时还做了额外的操作，比如判断数据类型，打印日志，做计算等。
        它可以作为别的类的类属性的一个"描述"。之所以使用描述符，是因为对于属性的描述不应该放在它所属的类中，而是应该放在另一个专门描述它的地方。
       （注意，是描述类属性，而不是对象属性！）

使用场景：1. 由于python是动态语言，python变量的类型需要等到赋值时才能控制。那么如何控制一个属性的类型呢？如果写在类属性的类中会显得很冗杂，这时可以
           把判断类型的逻辑写在另一个专门描述该属性的类中，这就是描述符。
        2. 当一个属性需要做一些额外处理的时候，比如计算，发日志等，都可以放在描述符里来做这些事情。
        3. 想设置不能被删除的时候，实现__delete__方法，并且抛出异常。
        4. 设置只读属性的时候，同时实现__get__, __set__方法，并且在__set__方法中抛出异常。
        5. staticmethod, classmethod, property等都是由描述符实现的。

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


# 但是要注意，单纯的实例属性是不能使用描述符的：描述符必须给类层面的属性使用：
class HumanWrong(object):

    def __init__(self):
        self.character = CharacterDescriptor("乐观的")


s2 = HumanWrong()
print(s2.character)
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


# 上面这样做的话也可以，但是会显得很冗余，更好的做法是把set，get的东西都写在描述符里
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


# 使用描述符后，测试类变得很纯净
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
print("------------------------------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------
# 通过实例调用时，属性查找的优先级为：
# 1. 数据描述符最高
# 2. 实例变量 a.__dict__["x"]
# 3. 非数据描述符
# 4. 类变量  type(a).__dict__["x"]（如果当前类没找会按照MRO顺序查找父类）
# 5. __getattr__(如果有)
# ------------------------------------------------------------------------------------------
# 数据描述符
class TestDescriptor(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("获取test name")
        return self.name

    def __set__(self, instance, value):
        print("修改test name")
        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError("name must be string")


# 非数据描述符
class TestDescriptor2(object):
    def __init__(self):
        self.score = 100

    def __get__(self, instance, owner):
        print("获取test score")
        return self.score


class TestOrder(object):
    name = TestDescriptor("Boboyoyo")  # 数据描述符属性
    score = TestDescriptor2()  # 非数据描述符属性
    height = 160  # 类属性


to = TestOrder()
print(to.name)  # 使用数据描述符，返回Boboyoyo
print(TestOrder.name)  # 使用数据描述符，返回Boboyoyo
to.name = "Max"  # 实例属性无法覆盖数据描述符，使用数据描述符，修改test name
print(to.name)  # 使用数据描述符，返回Max
print(TestOrder.name)  # 使用数据描述符，返回Max
print("-------")
print(to.score)  # 使用非数据描述符，返回 100
to.score = 180  # 非数据描述符被实例属性覆盖
print(to.score)  # 实例属性，返回180
print(TestOrder.score)  # 非数据描述符， 返回 100
print("------------------------------------------------------------------------------------------")


# 还有一种情况，当设置属性值时，如果实例属性和数据描述符重名时，也会优先使用数据描述符并调用__set__：
class M(object):

    def __init__(self):
        self.val = 10

    def __get__(self, instance, owner):
        print("get val")
        return self.val

    def __set__(self, instance, value):
        print("set val")
        self.val = value + 100


class A(object):
    x = M()

    def __init__(self, a):
        self.x = a  # self.x 这里是描述符对象，当给它设置值时调用__set__


aaa = A(20)  # 实例化对象，并设置初始值为20。这里其实就已经调用了数据描述符中的__set__函数。
print(aaa.x)  # 120
print("------------------------------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------
# 将描述符作为装饰器使用：例如python内置的property，class method等都是如此实现的。
# ------------------------------------------------------------------------------------------
# 以下是一个property描述符的等价实现：
class Property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Target(object):
    desc = "Amazing pyhton"

    def __init__(self, attr=5):
        self._x = attr

    @Property
    # 方法本质上也是类层面的属性，所以可以使用描述符
    def show(self):
        return self._x

    @show.setter
    def show(self, value):
        self._x = value

    @show.deleter
    def show(self):
        del self._x


# 实例化描述符对象t
t = Target()
# 当调用t.show时，首先因为描述器类作为装饰器装饰了show函数，所以执行show = Property(show)。
# 此时show指向Property的实例化对象，并且fget就是这个函数本身。
# 紧接着，因为Property是个描述符，所以这里直接执行__get__方法，这里的obj指的是t,所以执行self.fget(obj)，也就是调用show函数。
print(t.show)
# 当执行修改操作时，首先会使用show.setter作为装饰器，执行show = show.setter(show)。
# type函数返回这个对象的类，所以返回的是Property,然后再执行Property(self.fget, fset, self.fdel, self.__doc__)，把当前函数作为fset。
# 装饰器执行完毕后，执行__set__函数，对t.show进行修改。
t.show = 20
print(t.show)

