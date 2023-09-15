# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#
# p = Person("xm")
#
# print(p.__module__)
# print(p.__class__("x_m").name)   # Person("x_M")
# print(p.__class__.__name__.lower())
# print(p.__class__.__base__)


class Foo:

    __slots__ = ["a", "v"]

    def __init__(self):
        pass

f = Foo()
f.a = 100       # 没问题
print(f.a)
f.v = 100       # 报错 AttributeError: 'Foo' object has no attribute 'v'