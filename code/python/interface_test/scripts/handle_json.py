# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/5/12 9:36
@file: handle_json.py
"""
import json


class HandleJson:
    """处理json的类"""

    def __init__(self, file):
        self.file = file
        self.data = self.read_data()

    def read_data(self):
        with open(file=self.file) as fp:
            data = json.load(fp)
            return data

    def get_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    a = HandleJson(file="../datas/login.json")
    print(a.get_data(key='login'))
