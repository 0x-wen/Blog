# -*- coding: utf-8 -*-

"""
协程:是单线程下的并发,又称微线程,纤程。英文名Coroutine。协程是一种用户态的轻量级线程,即协程是由用户程序自己控制调度的。

并发的本质:切换+保存状态

在操作系统中
进程:是资源分配的最小单位
线程:是CPU调度的最小单位
协程:是单线程内实现并发切换执行任务
使用yield也可以实现在一个主线程中切换执行
"""

"""
# 1. yield from [生成器]  == 遍历f2获取到元素后通过yield返回生成器
# for value in f2():
#     yield value
# 2. 生成器可以通过next()获取到元素,但是如果生成器中没有元素了,会报错StopIteration
#   - 使用return会停止生成器,通过next()取值时会报错
"""


def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3


def func3():
    g = func1()    # 生成器函数在被调用时不会立即被执行,除非next(g)触发才被执行
    print(next(g))  # 开始执行func1()函数,但是遇到yield就会停止
    print(next(g))
    print(next(g))
    print(next(g))  # StopIteration


func3()  # 1,3,2
