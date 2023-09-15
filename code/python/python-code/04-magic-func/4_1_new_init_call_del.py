# -*- coding: utf-8 -*-
"""
__new__  实例化对象（1.创建对象 2.分配内存）
__init__ 构造方法,实例化对象时自动调用(1.可以没有 2.如果有方法必须返回None,默认不写return语句)
__call__ 对象可以被调用时触发执行
__del__  析构方法,当对象被回收时触发执行(程序结束、对象引用计数为零称为垃圾时)
"""


class MyClass(object):

    def __init__(self):
        print("__init__ is running...")

    def __new__(cls):
        print("__new__ is running...")
        return super().__new__(cls)  # 创建对象 分配内存

    def __call__(self, *args, **kwargs):
        print("__call__ is running...")

    def __del__(self):
        print("__del__ is running...")


MyClass()  # 匿名对象程序并未使用到,执行完后就销毁了
print("----------------------")

a = MyClass()  # 这里会先执行__new__ 在执行 __init__
assert hasattr(a, "__del__")  # True
print(callable(a))  # True  可以被调用时结果为True,对象如果没有__call__ 属性则是False
assert hasattr(lambda x, y: x + y, "__call__")  # True
print(callable(lambda x, y: x + y))  # True
