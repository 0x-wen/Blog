# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 11:48
# @Author  : Jw
# @File    : go_json_rpc.py
import itertools
import json
import socket


class JSONClient(object):
    def __init__(self, address):
        self.socket = socket.create_connection(address)
        self.id_counter = itertools.count(start=0, step=1)
        pass

    def __del__(self):
        self.socket.close()

    def __call__(self, method, *params):
        request = dict(id=next(self.id_counter), params=list(params), method=method)
        print("发送请求的数据信息:", request)
        self.socket.sendall(json.dumps(request).encode())

        response = self.socket.recv(4096)
        response = json.loads(response.decode())

        if response.get('id') != request.get('id'):
            raise Exception("expected id=%s, received id=%s: %s"
                            % (request.get('id'), response.get('id'),
                               response.get('error')))

        if response.get('error') is not None:
            raise Exception(response.get('error'))

        return response.get('result')


def test():
    request = {
        "id": 0,
        "params": ["imooc"],
        "method": "Test2.Name"
    }
    client = socket.create_connection(("localhost", 1234))
    client.sendall(json.dumps(request).encode())

    # This must loop if resp is bigger than 4K
    response = client.recv(4096)
    response = json.loads(response.decode())
    print(response)

    client.close()  # 关闭这个链接


if __name__ == '__main__':
    # test()
    client = JSONClient(("localhost", 1234))
    print(client("Test2.Name", "jw"))
    pass
