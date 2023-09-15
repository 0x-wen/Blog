# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 13:36
# @Author  : Jw
# @File    : public_random_func.py
import random
import string


def random_interface_data():
    """随机返回一些接口title"""
    names = ['登录', '购物车', '支付', '订单']
    for _ in range(20):
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        interface_title = random.choice(names) + random_str
    return interface_title
