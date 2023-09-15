# -*- coding: utf-8 -*-

import threading


class MyThread(threading.Thread):

    def __init__(self, args, **kwargs):  # 注意使用 args接收参数时形参 不需要增加*
        super(MyThread, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """线程启动的时候,会调用run方法"""
        for _ in range(5):
            print(f"{self.args[0]} 正在 听音乐.... 获得参数args:{self.args},kwargs:{self.kwargs}")


if __name__ == '__main__':
    tasks = []
    for i in range(3):
        t1 = MyThread(args=(f'张三{i}', 18), kwargs={"city": '深圳'})
        tasks.append(t1)

    for i in tasks:
        i.start()
    print("--------")
