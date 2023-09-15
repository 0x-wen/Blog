# -*- coding: utf-8 -*-

class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__bases__)  # (<class '__main__.A'>, <class '__main__.B'>)
