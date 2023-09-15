# -*- coding: utf-8 -*-
"""
生成器(高效): 生成器是特殊的迭代器,迭代器是特殊的可迭代对象,那么生成器必定是可迭代对象
使用yield关键字返回值是一个生成器对象
"""
from typing import Iterable, Iterator


def g_func2():
    my_list = range(3)
    for i in my_list:
        yield i * i


g = g_func2()

print(isinstance(g, Iterable))  # True
print(g.__iter__())  # <generator object g_func1 at 0x10271fc10>
print(next(g))
print(next(g))
print(next(g))
print(hasattr(g, "__iter__"))  # True
print(hasattr(g, "__next__"))  # True
print(isinstance(g, Iterator))  # True
