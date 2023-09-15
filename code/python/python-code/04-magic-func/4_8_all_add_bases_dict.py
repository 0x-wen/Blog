# -*- coding: utf-8 -*-
"""
__add__:  手动实现相加操作
__dict__: 获取对象的属性
__bases__: 获取类继承的元素
__all__: 当其它文件以“from 模块名 import *”的形式导入该模块时，该文件中只能使用 `__all__` 列表中指定的成员
"""


class MyClass(object):

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # other这里传入的是第二个对象 obj2  obj2.value ==》 __init__ 初始化中传入的value
        return self.value + other.value


a = MyClass(10)
print(a + MyClass(20))
print(MyClass.__dict__)


# __bases__  这是一个元祖，里面的元素是继承的类
class A(object):
    pass


print(A.__bases__)

# 当其它文件以“from 模块名 import *”的形式导入该模块时，该文件中只能使用 `__all__` 列表中指定的成员
__all__ = ["MyClass"]
