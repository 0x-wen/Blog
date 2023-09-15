# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/15 15:53
# @Author  : JW
# @FileName: index_datas.py
"""


class AddShop:
    """添加店铺测试数据"""
    add_shop_pass = {"shop_name": "北京烤鸭哟", "shop_detailed_address": "前门大街001号", "social_credit_code": "1234564512A1SDF",
                     "near": "靠近北京天安门", "check": "返回已认证商家"}

    add_shop_fail = [{"shop_name": "北京", "shop_detailed_address": "前门大街",
                      "social_credit_code": "1234564512A1SDF454545454545454545454545",
                      "near": "靠近北京天安门"},
                     {"shop_name": "油焖大虾哈哈哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇", "shop_detailed_address": "前门大街",
                      "social_credit_code": "1234564512A1SDF",
                      "near": "靠近北京天安门"}]


class JumpVipBackground:
    """跳转会员后台测试数据"""
    jump_vip_background_pass = {"check": "会员卡管理"}
