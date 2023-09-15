# -*- coding: utf-8 -*-

"""
测试有IO操作时,使用多个协程与单线程串行多个任务执行效率的对比
"""
import time

import gevent

from gevent import monkey

monkey.patch_all()


def task(args):
    time.sleep(1)
    print(args)


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    return wrapper


@count_time
def sync_func():
    """单线程 同步执行"""
    for i in range(3):
        task(i)


@count_time
def async_func():
    """单线程 异步执行"""
    g_lst = []
    for i in range(3):
        g_lst.append(gevent.spawn(task, i))  # 创建协程任务,传参数
    gevent.joinall(g_lst)


if __name__ == '__main__':
    print(sync_func())
    print(async_func())
