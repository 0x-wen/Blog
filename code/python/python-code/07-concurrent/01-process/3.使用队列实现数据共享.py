# -*- coding: utf-8 -*-
"""
如何使用队列实现进程间的数据共享？
    1.主进程创建一个队列 用于存储数据
    2.将队列对象 作为参数 传递给进程函数
    3.子进程函数中需要取出 队列中的值信息
    4.操作完队列数据之后，需要将值信息，推送到队列中
"""

import os
import time
from multiprocessing import Process, Queue
from multiprocessing.process import current_process


def work1(args):
    for _ in range(5):
        time.sleep(1)
        num = args.get()
        num += 1
        args.put(num)
        print(f"正在播放 无人之岛~~~子进程中的num值为:{num}, 当前进程名称：{current_process().name}")


def work2(args):
    for _ in range(7):
        time.sleep(1)
        num = args.get()
        num += 1
        args.put(num)
        print(f"正在专心 写代码中---子进程中的num值为:{num}, 当前进程名称：{current_process().name}")


def main():
    q = Queue()  # 进程安全的队列,在使用put 和 get 方法时,其内部会加锁
    q.put(0)
    p1 = Process(target=work1, args=(q,), name="听歌进程")
    p2 = Process(target=work2, args=(q,), name="工作进程")
    # p2.daemon = False
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"主进程中的num值为:{q.get()}, PID是:{os.getpid()}")
    pass


if __name__ == '__main__':
    main()
