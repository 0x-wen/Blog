# -*- coding: utf-8 -*-

"""
# 检查IO 遇到gevent.sleep() 协程会自动切换
# gevent()对普通的IO (比如time模块的sleep,socket 以及urllib request等网络请求)是无法切换的：
# gevent.sleep(2)模拟的是gevent可以识别的io阻塞,而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了
# from gevent import monkey;monkey.patch_all() 必须放到被打补丁者的前面,如time,socket模块之前
"""
import time

import gevent
from gevent import monkey

monkey.patch_all()  # 打上补丁之后,遇到time.sleep等 其他IO操作需要等待时 也会切换协程


def eat(name):
    print(f"eat 1 {name}")
    # time.sleep(5)
    gevent.sleep(2)
    print(f"eat 2 {name}")


def play(name):
    print(f"{name} play 1")
    # time.sleep(5)
    gevent.sleep(1)
    print(f"{name} play 2")


g1 = gevent.spawn(eat, "张三")
g2 = gevent.spawn(play, "张三")
gevent.joinall([g1, g2])  # 等价 ==》 g1.join() g2.join()
