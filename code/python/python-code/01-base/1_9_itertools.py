# -*- coding: utf-8 -*-
import itertools

# 为高效循环而创建迭代器的函数

iterable = itertools.chain(["A", "B", "C"], ["D", "E", "F"])
for i in iterable:
    print(i)  # --> A B C D E F

from_iterable = itertools.chain.from_iterable(['ABC', 'DEF'])
for i in from_iterable:
    print(i)

r = itertools.combinations("ABCD", 2)
for i in r:
    print(i)  # --> AB AC AD BC BD CD
