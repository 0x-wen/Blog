# -*- coding: utf-8 -*-

import asyncio
import time

num = 0


async def worker1(i):
    global num
    for item in range(i):
        num += 1
        print(f"worker1 is running i:{item}")


async def worker2(i):
    global num
    for item in range(i):
        num -= 1
        print(f"worker2 is running i:{item}")


async def main():
    print("开始多协程执行任务.")
    start_time = time.time()
    tasks1 = [asyncio.create_task(
        worker1(10000)), asyncio.create_task(worker2(10000))]

    await asyncio.gather(*tasks1)
    print(f"主线程执行完毕,耗时:{time.time() - start_time}, num:{num}")


asyncio.run(main())
