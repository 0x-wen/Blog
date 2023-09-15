# -*- coding: utf-8 -*-
"""
迭代器: 必须要同时拥有__iter__和__next__方法才是迭代器
"""
from typing import Iterator

my_iterator = iter(["1", "2", "3"])
# hasattr 判断某个对象是否包含某个属性信息
print(hasattr(my_iterator, "__iter__"))  # True
print(hasattr(my_iterator, "__next__"))  # True


# 手写实现一个迭代器
class Students(Iterator):
    def __init__(self):
        self.students = ["张三", "李四", "王五"]
        self.index = 0

    # 自动使用父类的__iter__

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]


my_iterator = Students()
print(my_iterator.__iter__())  # <__main__.Students object at 0x1009a7950>
print(isinstance(my_iterator, Iterator))  # True
for item in my_iterator:
    print(item)


class Students2(Iterator):
    def __init__(self):
        self.students = ["1", "2", "3"]
        self.index = 0

    # __iter__方法要求返回值必须是一个”迭代器“ (或者返回值必须要有 `__next__` 方法)
    def __iter__(self):
        return iter(self.students)  # 使用iter 会返回一个迭代器

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]


my_iterator2 = Students2()
print(my_iterator2.__iter__())  # <list_iterator object at 0x104f37fd0>
print(isinstance(my_iterator2, Iterator))  # True
print(next(my_iterator2))  # 1
print(next(my_iterator2))  # 2
# print(next(my_iterator2))  # raise StopIteration


class Next:
    def __init__(self, stop, start=-1):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start >= self.stop - 1:
            raise StopIteration
        self.start += 1
        return self.start


class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return Next(self.stop)


my_range = MyRange(5)  # <__main__.MyRange object at 0x1045029d0>
# False 断言它不是一个迭代器,但是它可以被for遍历,所以__iter__返回值有__next__方法也可以
print(isinstance(my_range, Iterator))
for item in my_range:
    print(item)  # 也可以通过 for 遍历


def my_while():
    start, stop = 0, 5
    my_range1 = MyRange(stop)
    numbers = my_range1.__iter__()  # 手动调用__iter__方法
    while start < stop:
        print(numbers.__next__())
        start += 1


my_while()
