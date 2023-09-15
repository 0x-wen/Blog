# -*- coding: utf-8 -*-
import time


def loger(func):
    def wrapper(*args):
        print("1 记录日志的代码...")
        result = func(*args)
        print("2 日志分析的代码...")
        return result

    return wrapper


# 编写一个计算方法执行耗时的装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        print("3 计算耗时开始")
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"{func.__name__}: 耗时: {end_time - start_time}")
        print("4 计算耗时结束")
        return result

    return wrapper


@loger
@timer
def add(*args, **kwargs):
    return sum(args)


print(add(11, 1))  # 执行顺序: 1 -> 3 -> func.__name__耗时 -> 4 -> 2 -> func执行结果
