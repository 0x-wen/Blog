# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 17:18
# @Author  : Jw
# @File    : 01.测试用例执行计数装饰器.py

#
# def count_num(number=0):  # 这里接收装饰器的参数
#     def inner(func):  # 接收被装饰的函数
#         def wrapper(*args, **kwargs):  # 这里接收被装饰函数的参数
#
#             if number > 0:  # 装饰器的参数在这里使用，用于判断
#                 pass
#             else:
#                 func(*args, **kwargs)
#                 number = number + 1
#
#         return wrapper  # 这里返回函数的包装器
#
#     return inner

number = 0  # 执行计数


def count_num(num=0):
    def inner(func):
        def wrapper(*args, **kwargs):
            while not num:
                return num + 1, func(*args, **kwargs)
                pass

        return wrapper

    return inner


@count_num(num=number)
def print_str():
    print(f'{number}')
    return "response"


build = print_str()
number = build[0]
response = build[1]
print(number, response)

a = print_str()
pass
