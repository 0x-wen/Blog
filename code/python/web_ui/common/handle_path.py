# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 16:34
# @Author  : JW
# @FileName: handle_path.py
"""
import os

# 获取文件夹路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)
# 异常截图路径
ERROR_IMG_DIR = os.path.join(LOGS_DIR, "error_img")
if not os.path.exists(ERROR_IMG_DIR):
    os.mkdir(ERROR_IMG_DIR)
# 测试图片存放地址
TEST_IMG_DIR = os.path.join(LOGS_DIR, "test_img")
if not os.path.exists(TEST_IMG_DIR):
    os.mkdir(TEST_IMG_DIR)
PAGE_LOCATORS_DIR = os.path.join(BASE_DIR, "page_locators")
PAGE_OBJECTS_DIR = os.path.join(BASE_DIR, "page_objects")
TEST_CASES_DIR = os.path.join(BASE_DIR, "test_cases")
TEST_DATAS_DIR = os.path.join(BASE_DIR, "test_datas")
TEST_REPORTS_DIR = os.path.join(BASE_DIR, "test_reports")

# 测试素材图片路径
PHOTO = os.path.join(TEST_IMG_DIR, "photo.png")
LOGO = os.path.join(TEST_IMG_DIR, "logo.jpg")
DETAILS = os.path.join(TEST_IMG_DIR, "details.jpg")
pass
