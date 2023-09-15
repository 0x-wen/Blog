# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 16:23
# @Author  :  Jw
# @File    : run.py
from datetime import datetime
import unittest
import os

from libs import HTMLTestRunnerNew
from tools.operate_config import do_config
from tools.constants import TEST_REPORTS_DIR, TEST_CASES_DIR

suite = unittest.defaultTestLoader.discover(start_dir=TEST_CASES_DIR, pattern="test*.py")

# 美化报告
report_html_name = os.path.join(TEST_REPORTS_DIR, do_config('FILE_PATH', 'report_html_name'))
report_html_name_full = report_html_name + '_' + datetime.strftime(datetime.now(), "%Y%m%d") + '.html'
with open(report_html_name_full, 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=do_config("REPORT", "verbosity"),
                                              title=do_config("REPORT", "title"),
                                              description=do_config("REPORT", "description"),
                                              tester=do_config("REPORT", "tester"))
    runner.run(suite)

pass
