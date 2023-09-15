# -*- coding: utf-8 -*-

# 两个方法都只是为了自定义对象的打印信息
# 当对象被打印时执行,一般默认先找str, str没有则使用repr
class A(object):

    def __init__(self):
        self.name = "李四"

    def __str__(self):
        print("__str__ is running ...")
        return "str"

    def __repr__(self):
        print("__repr__ is running ...")
        return ""


print(A())  # 默认为 <__main__.A object at 0x1043aa710>
