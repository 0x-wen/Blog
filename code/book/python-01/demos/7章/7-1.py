import time
from multiprocessing import Process


def func(name):
    print(f'{name} is start')
    time.sleep(2)
    print(f'{name} is done')


if __name__ == "__main__":
    for _ in range(10):
        p = Process(target=func, args=("xm",))
        p.start()

    print("主进程结束")


