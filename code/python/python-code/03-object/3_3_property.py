# -*- coding: utf-8 -*-
"""
1.将函数属性伪装成数据属性
2.统一数据属性的查、改、删操作
"""


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    # 当name 遇到赋值操作, 即 = 时触发被property.setter装饰的函数的执行
    @name.setter
    def name(self, value):
        self.__name = value

    # 当name 遇到删除操作，即 del 时触发property.deleter装饰的函数的执行
    @name.deleter
    def name(self):
        print('deleter')


obj1 = Person('abc')
print(obj1.name)
obj1.name = 'aaa'
print(obj1.name)
del obj1.name


