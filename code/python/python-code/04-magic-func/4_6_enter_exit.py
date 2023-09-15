# -*- coding: utf-8 -*-

"""
上下文管理器: 支持"上下文管理协议"的对象,包含 __enter__() 和 __exit__() 方法
with 可以操作一个 支持上下文管理协议的对象
"""


class MyOpen:
    def __init__(self, file_name: str, mode="r"):
        self.file = open(file_name, mode)

    def __enter__(self):
        print("进入with语句块时触发")
        return self.file  # 返回值赋值给 as后面的接收值

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with语句块时触发,不论with语句块是否有异常报错，__exit__都会被执行")
        self.file.close()


with MyOpen("test", "w") as f:
    f.write("hello world")
