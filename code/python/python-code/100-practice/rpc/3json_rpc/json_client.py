# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:37
# @Author  : Jw
# @File    : json_client.py
import jsonrpclib

# 1.建立连接
server = jsonrpclib.ServerProxy('http://localhost:8081')
# 2.调用func
print(server.add(5, 6, 7, 8))
