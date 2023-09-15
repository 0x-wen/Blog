# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:46
# @Author  : Jw
# @File    : zero_client.py
import zerorpc

"""一元调用"""

# c = zerorpc.Client()
# c.connect("tcp://127.0.0.1:4242")
# print(c.hello("RPC"))


"""流式响应"""

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

for item in c.streaming_range(10, 20, 2):
    print(item)
