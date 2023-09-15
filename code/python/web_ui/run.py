# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/14 14:29
# @Author  : JW
# @FileName: run.py
"""
import pytest

if __name__ == '__main__':
    pytest.main(['--resultlog=test_reports/report.log', '--junitxml=test_reports/report.xml', '--html=test_reports/report.html'])
