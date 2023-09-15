# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 17:43
# @Author  : Jw
# @File    : 1.httpserver.py
"""
使用HTTPserver实现rpc
1.一定会发起一个网络请求，一定会有一个网路连接(tcp/udp)
"""
# 01.把远程函数变成一个http请求

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl
import json

host = ('', 8003)


class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = dict(parse_qsl(parsed_url.query))

        a = int(qs.get("a", 0))
        b = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header('Content-Type', "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"result": a + b}).encode('utf8'))


if __name__ == '__main__':
    server = HTTPServer(host, TodoHandler)
    print("Starting server, Listen at: %s:%s" % host)
    server.serve_forever()
