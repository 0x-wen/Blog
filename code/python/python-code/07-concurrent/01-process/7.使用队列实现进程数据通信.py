# -*- coding: utf-8 -*-

import json
import multiprocessing
import time


class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        self.q.put(message)

    def receive(self):
        while True:
            print(f"receive is {self.q.get()}")

    def send_all(self):
        for i in range(10):
            self.q.put(i)
            time.sleep(0.5)


def main():
    work_obj = Work(multiprocessing.Queue())
    send = multiprocessing.Process(target=work_obj.send, args=("你好...",))
    recv = multiprocessing.Process(target=work_obj.receive)
    send_all_p = multiprocessing.Process(target=work_obj.send_all)

    recv.start()
    send.start()
    send_all_p.start()

    send_all_p.join()  # 因为这个进程执行的时间最长
    # recv.join()   # 死循环 条件一直成立
    recv.terminate()  # 退出程序


if __name__ == '__main__':
    main()
