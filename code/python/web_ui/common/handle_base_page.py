# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 17:25
# @Author  : JW
# @FileName: handle_base_page.py
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os
from selenium import webdriver

from common.handle_log import HandleLog
from common.handle_path import ERROR_IMG_DIR


class HandleBasePage(object):
    # 创建一个日志器对象
    do_log = HandleLog().get_logger()

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_click_element(self, locator: tuple, timeout=10, poll=0.5, model=None) -> WebElement:
        """等待元素可点击"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            return wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException):
            self.do_log.error("元素定位出错，具体元素是{}".format(locator))
            self.screen_shot(model_name=model)
            raise

    def wait_presence_element(self, locator: tuple, timeout=10, poll=0.5, model=None) -> WebElement:
        """等待元素存在"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            return wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.do_log.error("元素定位出错，具体元素是{}".format(locator))
            self.screen_shot(model_name=model)
            raise

    def wait_visibility_element(self, locator: tuple, timeout=10, poll=0.5, model=None) -> WebElement:
        """等待元素可见"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            return wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.do_log.error("元素定位出错，具体元素是{}".format(locator))
            self.screen_shot(model_name=model)
            raise

    def screen_shot(self, model_name):
        """截图，保存至指定位置"""
        if not model_name:
            model_name = "_"
        else:
            if not isinstance(model_name, str):
                model_name = str(model_name)
        current_time = datetime.strftime(datetime.now(), "%Y%m%d%H%M")
        return self.driver.save_screenshot(os.path.join(ERROR_IMG_DIR, model_name + current_time + ".png"))

    def switch_window(self, window_handles, name=None, timeout=20, poll=0.5):
        """切换窗口"""
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(EC.new_window_is_opened(window_handles))
        if not name:
            return self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.driver.switch_to.window(name)


if __name__ == '__main__':
    a = webdriver.Chrome()
    b = HandleBasePage(a)
    a.get(url="http://www.baidu.com")
    time.sleep(2)
    b.screen_shot()
