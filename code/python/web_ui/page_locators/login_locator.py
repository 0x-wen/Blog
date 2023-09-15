# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 17:57
# @Author  : JW
# @FileName: login_locator.py
"""
from selenium.webdriver.common.by import By


class LoginLocator:
    """登录页面元素定位"""
    # 用户名输入框
    username_input = (By.XPATH, '//*[@name="username"]')
    # 密码输入框
    password_input = (By.XPATH, '//*[@name="password"]')
    # 登录按钮
    login_button = (By.XPATH, '//span[contains(text(),"登")]')
    # 密码错误提示元素定位
    login_fail = (By.XPATH, '//*[@class="el-message__content"]')

