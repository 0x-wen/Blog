import time
from multiprocessing import Process


def func(name):
    print(f'{name} is start')
    time.sleep(2)
    print(f'{name} is done')


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        func(self.name)


if __name__ == "__main__":
    p = MyProcess("xm")
    p.start()

    print("主进程结束")