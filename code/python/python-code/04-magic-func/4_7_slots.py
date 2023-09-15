# -*- coding: utf-8 -*-
"""
该类实例只能创建__slots__中声明的属性，否则报错, 具体作用就是节省内存
"""
from memory_profiler import profile


class Test(object):
    __slots__ = ['a', 'name']

    def __init__(self, name):
        self.name = name


Test.c = 3  # 类属性仍然可以自由添加
t = Test("xx")
t.a = 1
print(t.c)  # 绕过限制就是给类添加属性
# t.b = 2  # AttributeError: 'Test' object has no attribute 'b'


class TestA(object):
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TestB(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


@profile
def func_02():
    temp = [TestA(i, i + 1, i + 2) for i in range(10000)]
    del temp
    temp = [TestB(i, i + 1, i + 2) for i in range(10000)]
    del temp


func_02()
