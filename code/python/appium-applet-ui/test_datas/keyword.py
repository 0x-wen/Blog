# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 18:55
# @Author  :  Jw
# @File    : keyword.py
class Search:
    """搜索中要使用到的数据"""

    # 首页搜索需要用的到信息
    search_keyword = "theinkeylist"

    # 品牌搜索需要用的到信息
    brand_search = "aesop"


class Address:
    """收货地址要使用到的数据"""
    user_address = []
    one_user_address = ('consignee=xiaoming,detailed_address=beijingcity,'
                        'phone_number=15055555555,mailbox=55555555@qq.com,title=test_case_1')
    two_user_address = ('consignee=xiaohua,detailed_address=beijingcity,'
                        'phone_number=15088888888,mailbox=88888888@qq.com,title=test_case_2')

    one = {i.split("=")[0]: i.split("=")[1] for i in one_user_address.split(",")}
    two = {i.split("=")[0]: i.split("=")[1] for i in two_user_address.split(",")}
    user_address.append(one)
    user_address.append(two)
    # print(type(one_user_address))
    # print(user_address)
