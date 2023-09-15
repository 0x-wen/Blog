# -*- coding: utf-8 -*-

import os
import time
from concurrent.futures import ThreadPoolExecutor


def work(args, **kwargs):
    time.sleep(2)
    print(f"接收到的参数args:{args}, kwargs:{kwargs}")
    return f'work 返回值{args[1]}'


def main():
    thread_executor = ThreadPoolExecutor(max_workers=3)
    future_list = []
    for i in range(8):
        future = thread_executor.submit(
            work, args=("张三", i), kwargs={"city": "深圳"})
        future_list.append(future)
        print(f'当前线程还没执行完 状态：{future.done()}')  # 任务还没有执行完时 返回False
    
    thread_executor.shutdown()

    for future in future_list:
        print(future.done())
        print(future.result())  # 获取任务的返回值信息


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f"耗时：{time.time() - start_time}")
