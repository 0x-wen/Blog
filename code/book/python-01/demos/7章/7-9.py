import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print("子线程:", n)
    time.sleep(2)
    return n ** 2


def call_back(future):
    print("call_back:", future.result())


# pool = ThreadPoolExecutor(5)
# for i in range(10):
#     pool.submit(task, i).add_done_callback(call_back)
#
# print("主线程结束")

pool = ThreadPoolExecutor(5)
rets = pool.map(task, range(10))
for ret in rets:
    print(ret)

print("主线程结束")
