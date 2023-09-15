# -*- coding: utf-8 -*-

# 给类添加装饰器
def class_name(cls):
    cls.name = "小明"
    return cls


@class_name
class A(object):
    pass


print(A.name)
