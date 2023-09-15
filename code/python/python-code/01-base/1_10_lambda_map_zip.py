# -*- coding: utf-8 -*-

# lambda表达式
y: any = lambda x: x + 1
print(y(10))

Students = [
    {"name": "a", "age": 18},
    {"name": "c", "age": 20},
    {"name": "b", "age": 19},
    {"name": "ca", "age": 19},
    {"name": "cb", "age": 19}
]
# 根据age排序,age一致时根据name排序
print(sorted(Students, key=lambda student: (student["age"], student["name"])))

# map 可迭代对象元素合并 返回新的map对象,按最短的对象合并
a = [1, 2, 3]
b = [4, 5, ]
# map(func, *iterables)
# func --> lambda a1, b1: (a1, b1)
# *iterables --> a, b
num1 = map(lambda a1, b1: (a1, b1), a, b)  # <map object at 0x109efed60>
for i in num1:
    print(i)  # (1, 4), (2, 5)

from functools import reduce

print(reduce(lambda x, y: x + y, range(1, 101)))  # 5050

print(list(filter(lambda x: x > 5, range(10))))  # <filter object at 0x106ad6c40>

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]  # 元素个数与最短的列表一致
