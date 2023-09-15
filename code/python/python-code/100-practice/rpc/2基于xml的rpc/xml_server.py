# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:07
# @Author  : Jw
# @File    : xml_server.py
from xmlrpc.server import SimpleXMLRPCServer
from functools import reduce


class Calculate:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return abs(x - y)

    def divide(self, x, y):
        return x / y

    def test1(self, *args):
        if args:
            result = reduce(lambda x, y: x + y, args)
        else:
            result = None
        return result


obj = Calculate()

# 1.定义一个server服务，指定ip/port
server = SimpleXMLRPCServer(("localhost", 8088))
# 2.将实例注册给rpc server
server.register_instance(obj)
# server.register_function(test1())
print("Listening on port 8088")
# 3.开启服务
server.serve_forever()
