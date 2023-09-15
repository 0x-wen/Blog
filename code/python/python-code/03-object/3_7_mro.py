# -*- coding: utf-8 -*-

class A1:
    pass


class A(A1):
    pass


class B:
    pass


class C(A, B):
    pass


# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.A1'>, <class '__main__.B'>, <class 'object'>]
print(C.mro())
