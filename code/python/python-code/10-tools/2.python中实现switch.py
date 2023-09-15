# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 14:38
# @Author  : Jw
# @File    : 2.python中实现switch.py

__doc__ = '类似实现switch的方式'

score = 90

switch = {
    90: lambda: 'A',
    80: lambda: 'B',
    70: lambda: 'C'
}

# 思考：假设其他分数都输出 D
grade = switch.get(40)
if grade is None:
    grade = lambda: 'D'

print(grade())


def mytest_1():
    print(f'{mytest_1.__name__}')
    pass


def mytest_2():
    print(f'{mytest_2.__name__}')


func_test = {
    '1': mytest_1,
    '2': mytest_2,
}


def switch_func(num):
    if num == '1':
        func_test[num]()
    elif num == '2':
        func_test[num]()


if __name__ == '__main__':
    switch_func('2')
