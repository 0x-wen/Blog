import asyncio
import time


async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(f1()),
    asyncio.ensure_future(f2()),
]

start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start)


