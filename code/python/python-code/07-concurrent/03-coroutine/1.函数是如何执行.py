# -*- coding: utf-8 -*-

import dis  # 反汇编包


def add(a, b):
    return a + b


def main(x, y):
    print("main is running...")
    a = 1
    return add(x, y), a


if __name__ == '__main__':
    print(main(33, 55))
    dis.dis(main)
    print(main.__code__.co_code)  # 返回一个二进制
    print(list(main.__code__.co_code))  # 转换为list
    print(dis.opname[116])  # LOAD_GLOBAL 0
    print(dis.opname[100])  # LOAD_CONST 1   都是指令和操作信息
    print(type(main.__code__))  # <class 'code'> __code__ 是 PyCodeObject对象,保存的是上下文信息,还有局部变量 常量 函数名等信息
    print(main.__code__.co_varnames)  # 变量  ('x', 'y', 'a', 'result')
    print(main.__code__.co_consts)  # 常量  (None, 'main is running...', 1)
    print(main.__code__.co_names)  # ('print', 'add')
