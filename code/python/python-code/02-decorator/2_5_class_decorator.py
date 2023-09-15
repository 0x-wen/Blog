# -*- coding: utf-8 -*-

# 使用类编写装饰器
class A:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("__call__ is running ...")
        return self.func(*args)


@A  # 本质获得一个a_obj = A(add)
def add(*args):
    return sum(args)


print(add(1, 2))
