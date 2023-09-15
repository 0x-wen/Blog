# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 17:12
# @Author  : Jw
# @File    : client.py
import grpc

from proto import helloworld_pb2, helloworld_pb2_grpc

# 1. 这个问题能改吗？
# 2. 其他语言有没有这个问题 其他语言 go语言 python 不服气
if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        hello_request = helloworld_pb2.HelloRequest()
        hello_request.name = "mysql"
        # hello_request.id.extend([1, 2])
        # hello_request.id.append(3)
        rsp: helloworld_pb2.HelloReply = stub.SayHello(hello_request,
                                                       metadata=(("username", "admin"), ("password", "admin123")))

        print(rsp.message)
