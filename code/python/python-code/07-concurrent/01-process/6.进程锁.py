# -*- coding: utf-8 -*-

import time
import multiprocessing


def work(name, _lock):
    _lock.acquire()  
    time.sleep(1)
    print(f"我是{name}...")
    _lock.release()  


def main():
    manger = multiprocessing.Manager()
    _lock = manger.Lock()

    pool = multiprocessing.Pool(2)
    for i in range(10):
        pool.apply_async(func=work, args=(i, _lock))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
    print("~~~~~~")
