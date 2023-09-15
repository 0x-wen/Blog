# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 18:23
# @Author  : JW
# @FileName: test_login.py
"""
import time

import pytest

from test_datas.login_datas import *


@pytest.mark.usefixtures("init_class")
@pytest.mark.usefixtures("init_fun")
class TestLogin:

    def test_login(self, init_fun):
        driver, login_page, index_page = init_fun
        login_page.user_login(username=login_pass["username"], password=login_pass["password"])
        assert login_pass["check"] in index_page.user_name_check()

    @pytest.mark.parametrize("data", login_fail)
    def test_login_fail(self, init_fun, data):
        driver, login_page, index_page = init_fun
        login_page.user_login(username=data["username"], password=data["password"])
        assert data["check"] in login_page.user_fail_check()
