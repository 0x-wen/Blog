# -*- coding: utf-8 -*-

from functools import wraps
from inspect import getfullargspec


def validate_input(obj, **kwargs):
    hints = obj.__annotations__

    for para_name, para_type in hints.items():
        if para_name == "return":
            continue
        if not isinstance(kwargs[para_name], para_type):
            raise TypeError(f"{para_name} 类型错误, 期望是: {para_type}")


def check_type(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))
        print(kwargs)

        validate_input(decorator, **kwargs)
        return decorator(**kwargs)

    return wrapped_decorator


@check_type
def add(a: int, b: int) -> int:
    return a + b


print(add(11, 1))


if __name__ == '__main__':
    print(add.__annotations__)
    pass
