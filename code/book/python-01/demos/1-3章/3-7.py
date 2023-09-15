g = (i for i in range(10))

# print(g)
# # for i in g:
# #     print(i)
#
# l = list(g)
# print(l)

# print(next(g))
# print(next(g))
# print(next(g))

def foo():
    for i in range(10):
        yield i

# g = foo()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))


for i in foo():
    print(i)