# -*- coding: utf-8 -*-

"""
进程间的数据是不共享的,需要实现数据共享,可采用队列的方式实现
"""

import os
import time
from multiprocessing import Process
from multiprocessing.process import current_process

num = 0


def work1():
    for _ in range(5):
        time.sleep(1)
        global num
        num += 1
        print(f"正在播放 无人之岛~~子进程中的num值为:{num}, 当前进程名称：{current_process().name}")


def work2():
    for _ in range(7):
        time.sleep(1)
        global num
        num += 1
        print(f"正在专心 写代码中---子进程中的num值为:{num}")


if __name__ == '__main__':
    p1 = Process(target=work1, name="听歌进程")
    p2 = Process(target=work2, name="工作进程")
    p2.daemon = False
    p1.start()
    p2.start()
    p1.join()
    # p2.join()
    print(f"hi... 我是主进程,我的主进程PID是:{os.getpid()}")
    print(f"主进程中的num值为:{num}")
