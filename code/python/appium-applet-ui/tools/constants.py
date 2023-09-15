# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 15:47
# @Author  :  Jw
# @File    : constants.py
import os

# 获取文件夹路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件CONFIGS_DIR路径
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
if not os.path.exists(CONFIGS_DIR):
    os.mkdir(CONFIGS_DIR)

# 配置文件test_case.ini路径
TEST_CASES_INI_PATH = os.path.join(CONFIGS_DIR, "test_case.ini")

LOGS_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

# 异常截图路径
ERROR_IMG_DIR = os.path.join(LOGS_DIR, "error_img")
if not os.path.exists(ERROR_IMG_DIR):
    os.mkdir(ERROR_IMG_DIR)

# 设置定位文件路径
LOCATORS_DIR = os.path.join(BASE_DIR, "locators")
if not os.path.exists(LOCATORS_DIR):
    os.mkdir(LOCATORS_DIR)

# 设置页面对象元素路径
ELEMENT_PAGES_DIR = os.path.join(BASE_DIR, "element_pages")
if not os.path.exists(ELEMENT_PAGES_DIR):
    os.mkdir(ELEMENT_PAGES_DIR)

# 设置测试用例文件路径
TEST_CASES_DIR = os.path.join(BASE_DIR, "test_cases")
if not os.path.exists(TEST_CASES_DIR):
    os.mkdir(TEST_CASES_DIR)

# 设置测试数据文件路径
TEST_DATAS_DIR = os.path.join(BASE_DIR, "test_datas")
if not os.path.exists(TEST_DATAS_DIR):
    os.mkdir(TEST_DATAS_DIR)

# yaml数据文件路径
YAML_DATA_PATH = os.path.join(TEST_DATAS_DIR, "devices_info.yaml")

# 设置测试报告文件路径
TEST_REPORTS_DIR = os.path.join(BASE_DIR, "test_reports")
if not os.path.exists(TEST_REPORTS_DIR):
    os.mkdir(TEST_REPORTS_DIR)

report_path = os.path.join(TEST_REPORTS_DIR, 'report')

pass
