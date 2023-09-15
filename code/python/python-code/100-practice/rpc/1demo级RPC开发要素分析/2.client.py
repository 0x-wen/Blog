# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 17:53
# @Author  : Jw
# @File    : 2.client.py
import requests


# 如果实现像本地调用方法一样，该如何处理？
# def add(a, b):
#     return a + b

class Client(object):
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        payload = {
            "method": "add",
            "params": [a, b],
            "jsonrpc": "2.0",
            "id": 0
        }
        response = requests.get(url=self.url).json()
        print(response)
        return response.get("result")


if __name__ == '__main__':
    client = Client("http://localhost:8003/?a=1&b=3")
    print(client.add(1, 2))
