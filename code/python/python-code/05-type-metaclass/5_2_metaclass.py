# -*- coding: utf-8 -*-

"""
1.所有类 如果不指定metaclass 默认都是通过type创建的
2.自定义某个元类 都是继承type,为了改变如何创建类,
作用:让创建的类 本来就具备各种属性或者方法，通过type创建的类都是空的
"""


class MyTypeClass(type):
    @classmethod
    def run(cls):
        print("创建的类 天生会跑...")

    @classmethod
    def eat(cls):
        print("使用MyTypeClass 创建的类，具备eat类方法...")

    def __new__(cls, name: str, bases: tuple, attrs: dict):
        """
        创建一个对象（使用type创建 对象 这个对象是一个类）
        :param name: 类名
        :param bases: 继承类1，继承类2
        :param attrs: __dict__属性
        """
        name = "Student"
        bases = (object,)
        attrs["city"] = "深圳"
        attrs["run"] = cls.run
        attrs["eat"] = cls.eat
        return type.__new__(cls, name, bases, attrs)


# metaclass 指定类是由谁创建,改变了创建类的方式
class A(object, metaclass=MyTypeClass):
    pass


class B(object):
    pass


# metaclass 指定类是由谁创建 默认值为type,所有的类都是由type创建的
class C(object, metaclass=type):
    pass


if __name__ == '__main__':
    print(A.__dict__)  # A类有哪些属性信息
    A.run()
    A.eat()
