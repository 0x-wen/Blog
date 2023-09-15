# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/19 14:10
# @Author  : JW
# @FileName: test_vip_index.py
"""
import unittest
from selenium import webdriver
import time


from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from page_objects.vip_index_page import VipIndexPage
from test_datas.login_datas import *


class TestIndex(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.vip_index_page = VipIndexPage(self.driver)
        self.driver.get("http://xxxxx.com")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
        pass

    def test_jump_vip_background(self):
        self.login_page.user_login(username=login_pass["username"], password=login_pass["password"])
        time.sleep(0.5)
        cur_handles = self.driver.window_handles
        self.index_page.jump_vip_background()
        self.index_page.switch_window(cur_handles)
        time.sleep(0.5)
        self.vip_index_page.get_members_activity_management.click()
        self.vip_index_page.scan_code_members_click()
        self.vip_index_page.add_activity()


if __name__ == '__main__':
    unittest.main()
