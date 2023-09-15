# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/5/14 19:51
@file: handle_context.py
"""
import re
import random
import string


class Context(object):
    """实现参数化"""

    label_name_pattern = re.compile(r'\$\{label_name\}')

    @staticmethod
    def random_label_name():
        label_name = "标签" + "".join(random.sample(string.ascii_uppercase, 5))
        return label_name

    @classmethod
    def label_name_replace(cls, data):
        if re.search(cls.label_name_pattern, data):
            data = re.sub(cls.label_name_pattern, cls.random_label_name(), data)
        return data

    @classmethod
    def parameterization(cls, data):
        """参数化"""
        data = cls.label_name_replace(data)
        return data


if __name__ == '__main__':
    str_1 = '{"name":"${label_name}"}'
    print(Context.parameterization(data=str_1))
