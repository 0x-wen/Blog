# -*- coding: utf-8 -*-
"""
1.引用计数:
sys.getrefcount() 获取对象的引用计数 在调用时会导致+1
由于循环引用的存在,对象a,b的引用都不为0,所以无法被回收
"""
import sys

a = [1, 2, 3]
b = a
c = b

# 输出对象的引用计数
print(sys.getrefcount(a))  # 输出：4

# 删除引用
# del a
del b
del c

# 输出对象的引用计数
print(sys.getrefcount(a))  # 输出：2


class A:
    def __init__(self):
        self.b = None


class B:
    def __init__(self):
        self.a = None


# 创建循环引用
a = A()
b = B()
a.b = b
b.a = a

del a
del b
