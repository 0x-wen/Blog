# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 18:12
# @Author  : JW
# @FileName: login_page.py
"""
from page_locators.login_locator import LoginLocator as locator
from common.handle_base_page import HandleBasePage


class LoginPage(HandleBasePage):

    def user_login(self, username, password):
        """
        用户登录流程
        :param username: 用户名
        :param password: 密码
        """
        self.driver.find_element(*locator.username_input).send_keys(username)
        self.driver.find_element(*locator.password_input).send_keys(password)
        self.wait_click_element(locator=locator.login_button, timeout=20, model="登录页面")
        self.driver.find_element(*locator.login_button).click()

    def user_fail_check(self):
        """登录失败验证"""
        self.wait_visibility_element(locator=locator.login_fail, model="登录失败提示")
        return self.driver.find_element(*locator.login_fail).text
