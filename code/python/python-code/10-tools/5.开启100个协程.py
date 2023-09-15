# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 16:48
# @Author  : Jw
# @File    : 5.开启100个协程.py
import asyncio
import time


# 编写定义启动协程的方法

async def work1():
    print("执行测试用例1")
    await asyncio.sleep(2)
    print("我是work1执行完毕")


async def work2():
    print("执行测试用例2")
    await asyncio.sleep(3)
    print("我是work2执行完毕")


async def start_task():
    print("开始多协程执行任务.")
    start_time = time.time()
    tasks1 = [asyncio.create_task(work1()), asyncio.create_task(work2())]

    await asyncio.gather(*tasks1)
    print(f"主线程执行完毕,耗时:{time.time() - start_time}")


asyncio.run(start_task())

# async def say_after(index):
#     while 1:
#         await asyncio.sleep(1)
#         print(f"{index}:hahah")
#         break
#
#
# tasks = []
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#     for i in range(100):
#         tasks.append(asyncio.create_task(say_after(i)))
#         # await say_after(2, 'world')
#
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())
