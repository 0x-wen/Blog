# -*- coding: utf-8 -*-

"""
线程不安全，多个线程争抢资源，会导致数据出错
需要加锁：
1. __lock = threading.Lock()  # 创建一把锁
2. with __lock:  # with可操作锁, with包含的代码在操作完成之后会自动释放
3. 加锁的目的是让在同一时间内,cpu只处理一个线程中的代码,防止同时修改一个变量
"""
import threading
import time

n = 2000000
__lock = threading.Lock()


def work1():
    for _ in range(100000):
        global n

        with __lock:  # __lock.acquire() 上锁  __lock.release() 释放
            n -= 1


def main():
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work1)
    t1.start()
    t2.start()
    t1.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码
    t2.join()  # 阻塞，主进程/主线程 会等待 子线程执行结束之后，在执行主线程代码
    print(n)
    print("hi... 我是主线程")
    print(dir(__lock))


if __name__ == '__main__':
    main()
