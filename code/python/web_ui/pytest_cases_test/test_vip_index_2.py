# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/19 14:10
# @Author  : JW
# @FileName: test_vip_index.py
"""
import time


class TestIndex:

    def test_jump_vip_background(self, vip_background_init):
        driver, vip_index_page = vip_background_init
        vip_index_page.get_members_activity_management.click()
        vip_index_page.scan_code_members_click()
        vip_index_page.add_activity()
        assert "活动添加成功" == vip_index_page.add_activity_check.text


