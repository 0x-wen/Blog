# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 18:23
# @Author  : JW
# @FileName: test_login.py
"""
import unittest
from selenium import webdriver
import time
import ddt

from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from test_datas.login_datas import *


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://xxxxx.com")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        self.login_page.user_login(username=login_pass["username"], password=login_pass["password"])
        self.assertIn(login_pass["check"], IndexPage(self.driver).user_name_check())

    @ddt.data(*login_fail)
    def test_login_fail(self, data):
        self.login_page.user_login(username=data["username"], password=data["password"])
        self.assertIn(data["check"], self.login_page.user_fail_check(), msg="登录失败验证")


if __name__ == '__main__':
    unittest.main()
