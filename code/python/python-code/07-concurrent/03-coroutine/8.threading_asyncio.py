import asyncio
import threading


async def coroutine_1():
    print("coroutine 1 started")
    await asyncio.sleep(1)
    print("coroutine 1 finished")


async def coroutine_2():
    print("coroutine 2 started")
    await asyncio.sleep(2)
    print("coroutine 2 finished")


async def coroutine_3():
    print("coroutine 3 started")
    await asyncio.sleep(3)
    print("coroutine 3 finished")


async def coroutine_4():
    print("coroutine 4 started")
    await asyncio.sleep(4)
    print("coroutine 4 finished")


def thread_1():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))


def thread_2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(coroutine_3(), coroutine_4()))


if __name__ == "__main__":
    print("main thread started")
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main thread finished")
