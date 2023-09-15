# -*- coding: utf-8 -*-

import multiprocessing
import time


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return wrapper


class MyProcess(multiprocessing.Process):

    def __init__(self, args, **kwargs):  # 注意使用args接收参数时,形参不需要增加*
        super(MyProcess, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """进程启动的时候,会调用run方法"""
        for _ in range(5):
            time.sleep(1)
            print(f"{self.args[0]}, 参数args:{self.args},kwargs:{self.kwargs}")


@count_time
def main():
    tasks = []
    for i in range(3):
        t1 = MyProcess(args=(f'张三{i}', 18), kwargs={"city": '深圳'})
        tasks.append(t1)
    
    [i.start() for i in tasks]
    for i in tasks:
        i.join()


if __name__ == '__main__':
    main()
