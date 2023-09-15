# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/4/29 11:35
@file: constants.py
"""
import os

# 获取文件夹路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_DIR = os.path.join(BASE_DIR, 'cases')
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
DATAS_DIR = os.path.join(BASE_DIR, 'datas')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# 拼接文件路径
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, 'test_case.conf')
TEST_DATAS_FILE_PATH = os.path.join(DATAS_DIR, 'cases.xlsx')

pass
