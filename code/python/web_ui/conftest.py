# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/21 16:54
# @Author  : JW
# @FileName: conftest.py
"""
import pytest
from selenium import webdriver
import time

from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from page_objects.vip_index_page import VipIndexPage
from test_datas.login_datas import *


@pytest.fixture()
def init_fun():
    """进入登录页面前置条件"""
    print("这是用例级别的fixture，开始")
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    driver.get("http://xxxxx.com")
    driver.maximize_window()

    yield driver, login_page, index_page

    driver.quit()


@pytest.fixture(scope="class")
def init_class():
    print("这是class级别的fixture，开始测试。。。")


@pytest.fixture()
def background_init():
    """进入后台主页前置条件"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    driver.get("http://xxxxxx.com")
    driver.maximize_window()
    login_page.user_login(username=login_pass["username"], password=login_pass["password"])
    yield index_page


@pytest.fixture()
def vip_background_init():
    """进入会员后台前置条件"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    vip_index_page = VipIndexPage(driver)
    driver.get("http://xxxxx.com")
    driver.maximize_window()
    login_page.user_login(username=login_pass["username"], password=login_pass["password"])
    cur_handles = driver.window_handles
    index_page.jump_vip_background()
    index_page.switch_window(cur_handles)
    time.sleep(0.5)
    yield driver, vip_index_page
    driver.quit()
