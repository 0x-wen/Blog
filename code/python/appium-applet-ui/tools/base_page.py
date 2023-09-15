# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 11:50
# @Author  :  Jw
# @File    : base_page.py
import os
import time
from datetime import datetime

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from tools.constants import ERROR_IMG_DIR
from tools.operate_log import OperateLog


class BasePage:
    """定义一个公共处理类，包含各种操作方法"""

    do_log = OperateLog().get_logger()  # 创建一个日志器对象
    time_sleep = 0.5

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 获取当前屏幕的宽和高
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']
        self.do_log.info("# 获取当前屏幕的宽{}和高{}".format(self.x, self.y))

    def wait_click_element(self, locator: tuple, timeout=10, poll=0.1, model=None) -> WebElement:
        """等待元素可点击"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            return wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException):
            self.do_log.error("元素定位出错，具体元素是：{}".format(locator))
            self.screen_shot(model_name=model)
            raise

    def wait_presence_element(self, locator: tuple, timeout=10, poll=0.1, model=None):
        """等待元素存在"""
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
            return wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.do_log.error("元素定位出错，具体元素是：{}".format(locator))
            self.screen_shot(model_name=model)
            raise

    def get_element(self, element):
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(element))

    def get_contexts(self):
        """获取上下文信息"""
        time.sleep(self.time_sleep)
        contexts = self.driver.contexts
        contexts_str = "".join(contexts)
        self.do_log.info("获取当前上下文信息contexts:%s" % contexts_str)
        return contexts if contexts else None

    def switch_to_context(self):
        """切换上下文 -1(WEBWEBVIEW)"""
        contexts = self.get_contexts()
        if contexts:
            self.driver.switch_to.context(contexts[-1])  # 切换进入webview
            time.sleep(self.time_sleep)
        self.do_log.info("打印当前的context:%s" % self.driver.current_context)

    def switch_to_app(self):
        """切换上下文 APPWEBVIEW"""
        contexts = self.get_contexts()
        if contexts:
            self.driver.switch_to.context(contexts[0])  # 切换进入APPWEBVIEW
            time.sleep(self.time_sleep)
        self.do_log.info("打印当前的context:%s" % self.driver.current_context)

    def get_all_handles(self):
        """获取所有窗口句柄"""
        all_handle = self.driver.window_handles
        all_handle_str = "".join(all_handle)
        self.do_log.info("打印所有的窗口句柄:%s" % all_handle_str)
        return all_handle

    def get_app_element(self, locator: tuple, model=None):
        """
        app原生应用索取元素
        注意事项：在定位app的元素时 请确保当前context是APPWEBVIEW
        """
        if locator is not None:
            by, local_by = locator[0], locator[1]
            try:
                if by == "id":
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'xpath':
                    return self.driver.find_element_by_xpath(local_by)
                else:
                    return self.driver.find_element_by_android_uiautomator(local_by)
            except Exception as e:
                locator_str = "".join(locator)
                self.do_log.error("未在app应用中找到元素,locator定位信息是:%s" % locator_str)
                self.do_log.error(e)
                self.screen_shot(model_name=model)
                return None
        else:
            return None

    def get_webview_element(self, locator: tuple, is_more=False):
        """
        在webview中查找元素，涉及到切换窗口handle
        locator: 元素定位信息
        :return 返回查找到的元素和当前的元素所在的窗口句柄
        """
        all_handles = self.get_all_handles()  # 获取所有的Handle
        result_element = None
        all_handles_len = len(all_handles)

        while all_handles_len > 0:  # 判断句柄个数大于0
            self.do_log.info("当前句柄的个数为:%d" % all_handles_len)
            for handle in all_handles:
                try:
                    self.driver.switch_to.window(handle)
                    time.sleep(1)
                    if is_more:  # 需要获取多个元素时
                        result_elements = self.driver.find_elements(*locator)
                        if result_elements:
                            self.do_log.info("获取到多个ele对象信息:%s" % result_elements.__str__())
                            if isinstance(result_elements, list):
                                one_num = len(result_elements)
                                self.do_log.info("多个ele对象长度:%s" % one_num)
                            self.do_log.info("元素查找成功，当前元素的窗口句柄:%s" % handle)
                            all_handles_len = -1  # 找到之后改变判断条件 跳出循环
                            break
                        else:
                            all_handles_len -= 1
                            self.do_log.info("找到元素信息为：空，剩下%d个句柄，将继续查找" % all_handles_len)
                    else:
                        result_element = self.driver.find_element(*locator)
                        if result_element:
                            self.do_log.info("获取到一个ele对象信息:%s" % result_element.__str__())
                            self.do_log.info("元素查找成功，当前元素的窗口句柄:%s" % handle)
                            all_handles_len = -1  # 找到之后改变判断条件 跳出循环
                            break
                        else:
                            all_handles_len -= 1  # 未找到就减少一个句柄
                            self.do_log.info("找到元素信息为：空，剩下%d个句柄，将继续查找" % all_handles_len)
                except Exception as e:
                    locator_str = "".join(locator)
                    all_handles_len -= 1
                    self.do_log.info("查找失败，剩下%d个句柄，将继续查找，locator:%s" % (all_handles_len, locator_str))

        if all_handles_len == -1:  # 找到之后返回element元素信息
            return result_elements if is_more else result_element
        else:
            self.do_log.info("已遍历所有句柄，未发现要找的元素，请检查元素定位信息")
            return None

    def screen_shot(self, model_name):
        """截图，保存至指定位置"""
        if model_name:
            if not isinstance(model_name, str):
                model_name = str(model_name)
        else:
            model_name = "___"
        # 以当前年月日为文件夹名称存储错误图片信息
        current_time_file = os.path.join(ERROR_IMG_DIR, datetime.strftime(datetime.now(), "%Y%m%d"))
        if not os.path.exists(current_time_file):
            os.mkdir(current_time_file)

        file_name = model_name + datetime.strftime(datetime.now(), "%H%M%S") + ".png"
        file_path = os.path.join(current_time_file, file_name)
        return self.driver.save_screenshot(filename=file_path)

    def swipe_down(self, t):
        """向下滑动比例 Y 从小到大"""
        x1 = int(self.x * 0.5)  # x坐标
        y1 = int(self.y * 0.25)  # 起始y坐标
        y2 = int(self.y * (0.25 + t))  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, 500)

    def swipe_up(self, t):
        """向上滑动比例 Y 从大到小"""
        x1 = int(self.x * 0.5)  # x坐标
        y2 = int(self.y * (0.25 + t))  # 起始y坐标
        y1 = int(self.y * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y2, x1, y1, 500)

    def swipe_left(self, t):
        """向左滑动比例 X 从大到小"""
        y1 = int(self.y * 0.5)  # y坐标
        x1 = int(self.x * (0.25 + t))  # 起始x坐标
        x2 = int(self.x * 0.25)  # 终点x坐标
        self.driver.swipe(x1, y1, x2, y1, 500)

    def swipe_right(self, t):
        """向右滑动比例 X 从小到大"""
        y1 = int(self.y * 0.5)  # y坐标
        x1 = int(self.x * 0.25)  # 终点x坐标
        x2 = int(self.x * (0.25 + t))  # 起始x坐标
        self.driver.swipe(x1, y1, x2, y1, 500)

    def swipe_screen(self, direction, t=0.5):
        """
        :direction 移动的方向，提供上下左右
        :t 移动的比例值
        """
        if direction == "up":
            self.swipe_up(t)
        elif direction == "down":
            self.swipe_down(t)
        elif direction == "left":
            self.swipe_left(t)
        elif direction == "right":
            self.swipe_right(t)
        else:
            self.do_log.info("\n请检查传入的direction，当前仅提供四种滑动屏幕方式")

    def click_confirm_button(self):
        confirm_x = int(self.x / 2) + 300
        confirm_y = int(self.y / 2) + 150
        self.do_log.info("# 确认按钮坐标为:{},{}".format(confirm_x, confirm_y))
        return confirm_x, confirm_y

    def click_bottom_menu(self, index: int, menu_num=5, menu_y=0):
        """
        点击小程序底部菜单坐标
        index: 菜单下标值 从1开始
        menu_num: 底部菜单个数 默认为5
        menu_y: 菜单 Y 轴坐标 默认为50
        :return 菜单 X,Y 轴坐标
        """
        space_between = int(self.x / menu_num)  # 菜单间距
        menu_y = int(self.y + menu_y)  # 菜单y轴坐标
        self.do_log.info("间距是space_between:{},菜单y轴坐标menu_y:{}".format(space_between, menu_y))

        if int(index) > int(menu_num):
            self.do_log.info("所取下标大于总个数: {} > {}".format(index, menu_num))
            return None

        if isinstance(index, int):
            if index == 1:
                one_x = self.index_space_between(space_between=space_between, index=index)
                self.do_log.info("# 第一个菜单坐标{},{}".format(one_x, menu_y))
                return one_x, menu_y
            elif index == 2:
                two_x = self.index_space_between(space_between=space_between, index=index)
                self.do_log.info("# 第二个菜单坐标{},{}".format(two_x, menu_y))
                return two_x, menu_y
            elif index == 3:
                three_x = self.index_space_between(space_between=space_between, index=index)
                self.do_log.info("# 第三个菜单坐标{},{}".format(three_x, menu_y))
                return three_x, menu_y
            elif index == 4:
                four_x = self.index_space_between(space_between=space_between, index=index)
                self.do_log.info("# 第四个菜单坐标{},{}".format(four_x, menu_y))
                return self.index_space_between(space_between=space_between, index=index), menu_y
            elif index == 5:
                five_x = self.index_space_between(space_between=space_between, index=index)
                self.do_log.info("# 第五个菜单坐标{},{}".format(five_x, menu_y))
                return five_x, menu_y
        else:
            self.do_log.info("参数index类型是：{} != int".format(type(index)))
            return None

    @staticmethod
    def index_space_between(space_between, index):
        """
        菜单下标大于1时,返回 X 坐标 = space_between / 2 + (index - 1) * space_between
        space_between: 菜单间距
        index: 菜单下标
        :return X轴坐标
        """
        if index == 1:
            return space_between / 2
        if index > 1:
            return space_between / 2 + (index - 1) * space_between

    @staticmethod
    def input_text_value(value: str):
        """输入框 输入值"""
        os.system("adb shell input text %s" % value)


class ExecuteTermination:
    """执行终端"""

    @staticmethod
    def execute_result(command):
        """返回执行结果"""
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == "\n":
                continue
            result_list.append(i.split('\n'))
        return result_list

    @staticmethod
    def execute(command):
        os.system(command)


if __name__ == '__main__':
    # BasePage().screen_shot(model_name="11")
    result_list1 = ExecuteTermination.execute_result(command='adb devices')
    print(result_list1)
