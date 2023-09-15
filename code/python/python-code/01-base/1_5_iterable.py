# -*- coding: utf-8 -*-
"""
可迭代对象: 可被 for 遍历都是可迭代对象。
1.实现了 __iter__ 方法，并且该方法返回一个迭代器对象。  
2.实现了 __getitem__ 方法，并且可以通过索引访问元素。
"""

# 一个对象如果只实现了 __iter__ 方法，但没有返回迭代器对象，那么它并不是一个可迭代对象。
from typing import Iterable


class Iterable1:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        # 返回的是一个列表,而不是一个迭代器对象
        return self.data


def t_func1():
    obj1 = Iterable1()
    assert isinstance(obj1, Iterable)  # True
    assert iter(obj1)  # iter() returned non-iterator of type 'list'


class Iterable2:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        # 返回的是一个迭代器对象
        return iter(self.data)


def t_func2():
    obj2 = Iterable2()
    assert isinstance(obj2, Iterable)  # True
    print(iter(obj2))


t_func2()


class Iterable3:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, index):
        # 通过索引访问元素，实现迭代行为
        return self.data[index]


my_iterable = Iterable3()
print(iter(my_iterable))
