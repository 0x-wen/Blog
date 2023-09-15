# -*- coding: utf-8 -*-

"""
基本概念：
- 进程是系统资源分配的基本单元,线程是cpu调度和分配的基本单元,线程是由操作系统调度,协程由用户调度
- 进程拥有资源(CPU、内存)等,同一进程中的线程共享进程资源
- 多线程的切换速度比多进程快,消耗的资源更少
- 一个进程默认会有一个主线程(也称为主执行线程),主线程负责创建和管理其他线程，并在需要时进行协调和同步
- 由于 GIL 的存在，对于 CPU 密集型任务（例如计算密集型的循环运算），多个线程并不能同时利用多个 CPU 核心来并行执行，而是会在单个 CPU 核心上轮流执行
- 对于 I/O 密集型任务（例如网络请求、文件读写等），多线程在某些情况下仍然可以提高性能。当一个线程在等待 I/O 操作完成时，其他线程可以继续执行，从而充分利用 CPU 时间
"""
import threading
import time


def work1():
    for _ in range(5):
        time.sleep(1)
        print("我是：{},获取当前线程name:{} 在播放音乐...".format(work1.__name__, threading.current_thread().name))


def work2(*args, **kwargs):
    for _ in range(7):
        time.sleep(1)
        print(f"{work2.__name__}:获取到args参数信息:{args}, 获取到kwargs:{kwargs}")
        print(f"我是：{work2.__name__}, 获取当前线程name:{threading.current_thread().name} 在用心工作...")


def main():
    t1 = threading.Thread(target=work1, name='线程1')
    t2 = threading.Thread(target=work2, args=(18, 20), kwargs={"city": "深圳"}, name='线程2')
    t1.start()
    t2.start()
    t1.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码
    t2.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码
    print("hi... 我是主线程")


if __name__ == '__main__':
    main()
