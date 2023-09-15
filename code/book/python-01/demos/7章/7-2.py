import time
from multiprocessing import Process


def func(name):
    print(f'{name} is start')
    time.sleep(10)
    print(f'{name} is done')


if __name__ == "__main__":
    start = time.time()
    ps =[]
    for _ in range(10):
        p = Process(target=func, args=("xm",))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()

    end = time.time()
    print("主进程结束：", end - start)



