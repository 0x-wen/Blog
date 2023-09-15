# -*- coding: utf-8 -*-

"""
1.什么是进程池？  提前创建好一定数量的进程，进程池内的进程避免了创建与关闭的消耗
任务有多个 如果进程池中的进程没有空闲，任务则会等待。等到有空闲的进程，才会执行任务。

2.进程池的创建:multiprocessing
Pool函数()  设置最大进程数

3.pool.close() 进程池对象关闭
  pool.join()  等待进程池内进程执行完才执行主程序

4.pool.apply_async(func=work, args=(i,))  # 异步添加任务
  # 使用get()可以获得进程对象的返回值信息
"""

import multiprocessing
import os
import time


def work(count):
    time.sleep(2)
    return f'当前进程是:{count},进程ID:{os.getpid()}'


def main():
    pool = multiprocessing.Pool(4)
    result_list = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i,))  # 异步添加任务
        result_list.append(result)
    for res in result_list:
        print(res.get())  # 异步使用get()可以获得进程对象的返回值

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
