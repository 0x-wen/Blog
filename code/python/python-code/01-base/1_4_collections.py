# -*- coding: utf-8 -*-
# 这个模块实现了一些专门化的容器，提供了对 Python 的通用内建容器 dict、list、set 和 tuple 的补充。
from collections import namedtuple, deque, ChainMap

Student = namedtuple('Students', ["name", "age", 'index'])
tu1 = Student(name="张三", age=18, index=1)
print(tu1.name)  # 张三
print(isinstance(tu1, tuple))  # True 也是元祖类型数据
print(type(tu1))  # tu1数据类型 <class '__main__.Students'> Student对象

# deque 双端队列
d = deque('ghi')
d.extendleft('123', )
d.appendleft('4')
print(d)  # deque(['4', '1', '2', '3', 'g', 'h', 'i'])

# ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图
dict1 = {'music': 'bach', 'art': 'rembrandt'}
dict2 = {'art': 'van gogh', 'opera': 'carmen'}
dict3 = {'opera': 'dict3', 'test': 'dict3'}
c = ChainMap(dict1, dict2, dict3)
# 获取map中的key和其传入参数有关系, 迭代顺序是通过从后往前扫描
print(c.get('art'), c.get('opera'))  # rembrandt, carmen
# 如果要实现dict.update功能,可以使用update()
c.update(dict3)
print(c.get('art'), c.get('opera'))  # rembrandt, dict3
