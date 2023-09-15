# -*- coding: utf-8 -*-

# import 私有变量
# 1. __name它不会被导入到导入模块的命名空间中
# 2. _name会被导入到导入模块的命名空间中

class MyClass:
    def __init__(self):
        self.__name = "Private Name"  # 私有变量 __name
        self._name = "Conventionally Private Name"  # 约定上的私有变量 _name

    def get_private_name(self):
        return self.__name

    def get_conventionally_private_name(self):
        return self._name


obj = MyClass()

# 访问私有变量 __name
print(obj.get_private_name())  # 输出: Private Name
# print(obj.__name)  # 错误，在类外部，无法直接访问私有变量，会引发 AttributeError 错误
print(obj._MyClass__name)  # 输出: Private Name，通过名称重整方式访问私有变量

# 访问约定上的私有变量 _name
print(obj.get_conventionally_private_name())  # 输出: Conventionally Private Name
print(obj._name)  # 输出: Conventionally Private Name，可以直接访问约定上的私有变量
