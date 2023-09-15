# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/4/29 11:34
@file: run.py
"""
from datetime import datetime
import unittest
import os

from libs import HTMLTestRunnerNew
from scripts.handle_config import do_config
from scripts.constants import REPORTS_DIR, CASES_DIR

suite = unittest.defaultTestLoader.discover(start_dir=CASES_DIR, pattern="test*.py")

# 美化报告
report_html_name = os.path.join(REPORTS_DIR, do_config('FILE_PATH', 'report_html_name'))
report_html_name_full = report_html_name + '_' + datetime.strftime(datetime.now(), "%Y%m%d") + '.html'
with open(report_html_name_full, 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=do_config("REPORT", "verbosity"),
                                              title=do_config("REPORT", "title"),
                                              description=do_config("REPORT", "description"),
                                              tester=do_config("REPORT", "tester"))
    runner.run(suite)

pass
