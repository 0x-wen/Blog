# -*- coding: utf-8 -*-


def add(*args):
    return sum(args)


# 把函数当做参数,传递给另外一个函数
def new_add(func, *args):
    return f"对原函数进行装饰 遵循开放封闭原则{func(*args)}"


print(new_add(add, 1, 2, 3))
