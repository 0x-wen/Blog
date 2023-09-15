# -*- coding: utf-8 -*-

"""
GIL: 全局"解释器"锁
线程占用cpu:无论是单/多核cpu 同一时间内只有一个线程在使用cpu

cpu密集型场景:不合适使用多线程,python不能利用多核(GIL决定的)
io密集型场景:使用多线程可以节省时间
"""
import time
import threading


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


num = 0
__lock = threading.Lock()


@count_time
def work1():
    global num
    for _ in range(10000000):
        num += 1


def work2():
    global num
    with __lock:
        for _ in range(5000000):
            num += 1


@count_time
def main():
    t1 = threading.Thread(target=work2)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    work1()
    print(num)
    main()
    print(num)
