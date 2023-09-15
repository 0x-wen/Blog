# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:46
# @Author  : Jw
# @File    : zero_server.py
import zerorpc


# 一元调用
class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name


# 流式响应
class StreamingRPC(object):
    @zerorpc.stream  # @zerorpc.stream这里的函数修饰是必须的，否则会有异常，如TypeError: can’t serialize
    def streaming_range(self, fr, to, step):
        return range(fr, to, step)


s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
