# -*- coding: utf-8 -*-


# 编写一个带参数的装饰器，用于验证用户登录
def login_verify(is_login=False):  # 这里接收装饰器的参数
    def inner(func):  # 接收被装饰的函数
        def wrapper(*args, **kwargs):  # 这里接收被装饰函数的参数
            if is_login:  # 装饰器的参数在这里使用，用于判断
                print("被装饰函数执行前")
                result = func(*args)
                print("被装饰函数执行后")
                return result
            else:
                return None

        return wrapper  # 返回函数的包装器

    return inner


@login_verify(is_login=True)
def add(*args, **kwargs):
    return sum(args)


print(add(11, 22))
