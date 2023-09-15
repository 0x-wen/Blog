# def add(x: int, y: int) -> int:
#     return x + y
#
# func = add
#
# print(func(3, 4))
#
# funcs = [add]
#
# for f in funcs:
#     print(f(1, 8))
#

# def func(x):
#     return x + 1
#
#
# def add(x, f):
#     return f(x)
#
#
# print(add(10, func))


def add(x, y):
    return x + y


def foo():
    return add


f = foo()
print(f(1, 4))