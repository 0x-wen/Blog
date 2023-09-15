# -*- coding: utf-8 -*-
# 使用类实现装饰器 带参数
class S:
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __call__(self, *args, **kwargs):
        print("类装饰器转入的参数", self.name)
        print("1 装饰函数执行之前")
        result = self.func(*args)
        print("2 装饰函数执行之后")
        return result


def add(*args):
    return sum(args)


s = S(add, "hello")
print(s(1, 3))
