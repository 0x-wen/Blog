# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 10:09
# @Author  : Jw
# @File    : xml_client.py
from functools import reduce
from xmlrpc import client

# 1.建立一个连接
server = client.ServerProxy("http://localhost:8088")


# 2.使用实例 调用服务端暴露出来的func
# print(server.add(2, 3))
print(server.test1(2,3,4,5,5,6,))

# 基于xml的rpc 分析：
# 1.编码解码 肯定是基于xml
# 2.传输协议 是基于tcp协议连接
# 3.怎么定义call—id 其内部框架帮我们处理了这件事，主要是在server中将要调用的func暴露出来



