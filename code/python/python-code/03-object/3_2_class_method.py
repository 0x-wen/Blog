# -*- coding: utf-8 -*-
"""
classmethod 给类定义的方法
staticmethod 目的只是封装在一起,内聚
"""


class Person(object):

    def __init__(self, name):
        self.name = name

    @classmethod
    def name(cls, name):
        return cls(name)

    @staticmethod
    def age(age: int):
        return age

    def __repr__(self):
        return self.name


a = Person(name="张三")
print(a)
b = Person.name("李四")
print(b)
print(a.age(18))  # 对象可以调用
print(Person.age(20))  # 类也可以调用
