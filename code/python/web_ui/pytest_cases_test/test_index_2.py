# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 15:27
# @Author  : JW
# @FileName: test_index.py
"""
import time
import pytest

from test_datas.index_datas import AddShop as AS, JumpVipBackground as JVB


class TestIndex:

    def test_jump_vip_background(self, vip_background_init):
        """测试跳转至会员后台主页"""
        driver, vip_index_page = vip_background_init
        assert JVB.jump_vip_background_pass["check"] == vip_index_page.vip_background_check.text, "跳转至会员后台主页失败"
        # 调用添加会员卡点击事件
        # vip_index_page.add_vip_card_click.click()
        # time.sleep(3)

    @pytest.mark.success
    def test_add_shop(self, background_init):
        index_page = background_init
        index_page.get_shop_management.click()
        index_page.get_pass_shop.click()
        index_page.add_shop()
        time.sleep(0.2)
        index_page.add_shop_input_information(shop_name=AS.add_shop_pass["shop_name"],
                                              shop_detailed_address=AS.add_shop_pass["shop_detailed_address"],
                                              social_credit_code=AS.add_shop_pass["social_credit_code"],
                                              near=AS.add_shop_pass["near"])
        time.sleep(1)
        index_page.add_shop_input_information_2()
        time.sleep(0.5)
        assert AS.add_shop_pass["check"] == index_page.add_shop_check.text

    @pytest.mark.parametrize("data", AS.add_shop_fail)
    def test_add_shop_fail(self, background_init, data):
        index_page = background_init
        index_page.get_shop_management.click()
        index_page.get_pass_shop.click()
        index_page.add_shop()
        time.sleep(0.2)
        index_page.add_shop_input_information(shop_name=data["shop_name"],
                                              shop_detailed_address=data["shop_detailed_address"],
                                              social_credit_code=data["social_credit_code"],
                                              near=data["near"])
        time.sleep(1)
        index_page.add_shop_input_information_2()
        time.sleep(0.5)
