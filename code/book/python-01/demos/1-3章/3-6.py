# def add(x, y, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(sum(args))
#
#
# add(x=1, y=2, c=20)

# def f(x, y):
#     print(x + y)
#
#
# two_nums = (1, 2)
#
# x, y = two_nums
#
# f(*two_nums)  # f(1, 2)

def f(x, y):
    print(x + y)

nums = {"x": 3, "y": 5}
f(**nums)   # f(x=3, y=5)