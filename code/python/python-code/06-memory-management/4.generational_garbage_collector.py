# -*- coding: utf-8 -*-
"""
分代回收: 0 代、1 代和 2 代。
新创建的对象被放置在 0 代，如果在垃圾回收过程中保持存活，它们会逐渐晋升到更高的代。
"""
import ctypes
import gc

print(gc.get_threshold())  # 获取各代的阀值 (700, 10, 10)
gc.set_threshold(500, 20, 20)


# We are using ctypes to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # Disable generational gc

lst = []
lst.append(lst)

# Store address of the list
lst_address = id(lst)

# Destroy the lst reference
del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

# Destroy references
del object_1, object_2

# Uncomment if you want to manually run garbage collection process
gc.collect()

# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)
print(gc.get_stats())

# 'collections'：表示该代别进行的垃圾回收次数。
# 'collected'：表示在该代别中被回收的对象数量。
# 'uncollectable'：表示在该代别中无法回收的对象数量。

# [{'collections': 11, 'collected': 127, 'uncollectable': 0},
# 这表示在 0 代别进行了 11 次垃圾回收，共回收了 127 个对象，而没有无法回收的对象。
#  {'collections': 1, 'collected': 6, 'uncollectable': 0},
# 这表示在 1 代别进行了 1 次垃圾回收，共回收了 6 个对象，而没有无法回收的对象。
#  {'collections': 1, 'collected': 3, 'uncollectable': 0}]
# 这表示在 2 代别进行了 1 次垃圾回收，共回收了 3 个对象，而没有无法回收的对象。
