# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/4/29 18:19
@file: handle_request.py
"""
import requests
import json

from scripts.handle_log import do_log


class HttpRequest:
    """处理http请求"""

    def __init__(self):
        self.one_session = requests.session()

    def __call__(self, method, url, data=None, is_json=False, **kwargs):
        method = method.lower()
        if method == 'get':
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'post' or method == "patch" or method == "delete" or method == "put":
            if is_json:
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            do_log.error("检查请求方式是否支持")

        return res

    def close(self):
        """关闭会话"""
        self.one_session.close()


if __name__ == '__main__':
    url = ""
    data = {}
    headers = {"Content-Type": "application/json",
               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    res = HttpRequest()(method='post', url=url, data=data, is_json=True, headers=headers)
    print(res.text)
