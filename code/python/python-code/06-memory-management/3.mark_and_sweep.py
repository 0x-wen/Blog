# -*- coding: utf-8 -*-
"""
垃圾回收器中的标记清除算法首先从根对象开始遍历，标记所有可以访问到的对象，然后清除所有未标记的对象。
"""

import gc


class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Deleting {self.name}")


# 创建循环引用
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj1.other = obj2
obj2.other = obj1

# 手动触发垃圾回收
gc.collect()

# 删除对象引用
del obj1
del obj2

# 手动触发垃圾回收
gc.collect()
