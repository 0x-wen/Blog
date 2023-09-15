# -*- coding: utf-8 -*-

"""
一个正在运行的软件,最少会生成一个进程。进程是cpu分配资源的最小单位。
进程执行过程： 加载软件代码到内存 ==》 cpu为进程建立"档案"(pid)  ==》 等待时间片  ==》 退出
进程的状态： 创建 ==》 就绪  ==》 执行  ==》 阻塞  ==》 终止

p1.join()  # p1是子进程,主进程会等待p1结束后,在运行主进程代码
设置守护进程 ==True  主进程结束子进程也结束
           ==False 主进程等待子进程结束之后才结束

怎么完成进程之间的数据共享？
在主进程中创建队列,将队列作为参数,传递给子进程,子进程取出值后进行操作,可实现进程间数据共享。

演示demo,p1和p2 都依次使用了join() 所以是p1操作完成之后p2才会进行操作? 不是 p1和p2都是同时运行。

操作系统如何管理进程：
分配内存给进程,分配时间片给进程,存储进程信息(pid标识进程,为进程设置优先级,状态等等)
"""
import os
import time
from multiprocessing import Process


def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return end - start

    return wrapper


def work_01(user):
    for i in range(5):
        time.sleep(1)
        print(f" 我是:{user} 在听音乐,我的进程pid是{os.getpid()},我的父级pid是: {os.getppid()}")


def work_02(user):
    for j in range(8):
        time.sleep(1)
        print(f" 我是:{user} 在工作,我的进程pid是{os.getpid()},我的父级pid是: {os.getppid()}")


@count_time
def main():
    p1 = Process(target=work_01, args=("张三",), name="听歌进程")
    p2 = Process(target=work_02, args=("张三",), name="工作进程")
    # p2.daemon = True  # 设置守护进程
    p1.start()
    p2.start()
    p1.join()
    # p2.join()
    print(f"hi... 我是主进程,我的主进程PID是:{os.getpid()}")


if __name__ == '__main__':
    print(main())
