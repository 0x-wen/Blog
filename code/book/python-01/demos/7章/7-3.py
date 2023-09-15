import time
from multiprocessing import Process


def func(i):
    print(f'{i} is start')
    time.sleep(10)
    print(f'{i} is done')


if __name__ == "__main__":
    for i in range(4):
        p = Process(target=func, args=(i,))
        if i == 2:
            p.daemon = True
        p.start()
    time.sleep(2)
    print("主进程结束")



