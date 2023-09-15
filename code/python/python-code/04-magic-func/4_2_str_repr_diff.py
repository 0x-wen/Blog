# -*- coding: utf-8 -*-

"""
1.__new__ 创建对象，分配内存，把对象传递给 __init__
2.__init__ 初始化对象的时候执行，执行一些对象初始化操作
3.__str__ 打印对象时执行，返回值必须是 str类型
4.__repr__ 解释器在执行代码时会执行 __repr__ or 没有__str__时 repr会被执行
"""


class MyClass(object):
    def __str__(self):
        return "__str__ is running..."

    def __repr__(self):
        return "__repr__ is running..."


if __name__ == '__main__':
    a = MyClass()
    print(a)  # 这个时候 __str__ 被调用执行

""":terminal 代码
class A():
    def __repr__(self):
        return "__repr__ is running..."
    
    def __str__(self):
        return "__str__ is running..."

a=A()
a  # "__repr__ is running..."
print(a)  # "__str__ is running..."
"""
