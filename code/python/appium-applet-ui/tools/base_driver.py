# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 18:29
# @Author  :  Jw
# @File    : base_driver.py
import time

from appium import webdriver

from tools.constants import YAML_DATA_PATH
from tools.operate_yaml import OperateYaml

operate_yaml_o = OperateYaml()


def android_driver(i):
    """定义一个ChromeDriver"""
    # 配置appium兼容性参数  android/ios 版本等

    devices = operate_yaml_o.get_value('user_info_' + str(i), 'deviceName')
    port = operate_yaml_o.get_value('user_info_' + str(i), 'port')

    desired_cap = {}
    desired_cap["platformName"] = "Android"  # 指定测试平台
    desired_cap["platformVersion"] = "9"  # 指定移动端版本号
    desired_cap["deviceName"] = devices  # 指定设备名称
    desired_cap["appPackage"] = "com.tencent.mm"  # 指定启动包
    desired_cap["appActivity"] = ".ui.LauncherUI"  # 指定启动主类
    desired_cap["udid"] = devices  # 指定设备编号
    # desired_cap["udid"] = "emulator-5554"  # 模拟器
    # desired_cap["udid"] = "AKC7N18709002560"  # 华为p20 AKC7N18709002560
    # desired_cap["automationName"] = "uiautomator2"  # 默认是Appium 使用Uiautomator2才能抓取tost弹窗
    desired_cap["unicodeKeyboard"] = True  # 使用unicodeKeyboard的编码方式来发送字符串
    desired_cap["resetKeyboard"] = True  # 将键盘给隐藏起来
    desired_cap["noReset"] = True  # 是否重置
    # chromedriverfilepath的版本需要用在inspect中看到的版本
    desired_cap["chromedriverExecutable"] = "/Applications/Appium.app/Contents/Resources/app/node_modules/appium" \
                                            "/node_modules/appium-chromedriver/chromedriver/mac/chromedriver-77"
    desired_cap["recreateChromeDriverSessions"] = True  # recreateChromeDriverSessions 用于自动化配置X5内核驱动

    # 小程序单独运行在其他进程中，需要显示指定运行进程
    desired_cap["chromeOptions"] = {"androidProcess": "com.tencent.mm:appbrand0", 'w3c': False}

    # 实例化webdriver(连接地址win和Mac不同)
    driver = webdriver.Remote('http://0.0.0.0:' + port + '/wd/hub', desired_cap)
    time.sleep(3)
    return driver
