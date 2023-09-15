# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:37
# @Author  : Jw
# @File    : json_server.py
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from functools import reduce


def add(*args):
    if args:
        result = reduce(lambda x, y: x + y, args)
    else:
        result = None
    return result


# 1.监听端口
server = SimpleJSONRPCServer(('localhost', 8081))
# 2.注册暴露方法
server.register_function(add)
# 3.启动服务
server.serve_forever()
