from concurrent.futures import ThreadPoolExecutor
import time
import random


def task(n):  # 处理任务的函数
    time.sleep(random.randint(1, 5))
    return n ** 2


def call_back(future):		# 需要定义一个形参，这个形参是future，通过future.result()获取任务执行返回值。
    print('call_back>>>:', future.result())


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    # for i in range(1, 10):
    #     pool.submit(task, i).add_done_callback(call_back)
    #     # 给任务绑定回调函数，任务结束后自动调用回调函数，并将future对象当实参传给回调函数。

    rets = pool.map(task, range(1, 10))	
    for r in rets:
        print(r)
