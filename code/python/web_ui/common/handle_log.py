# -*- coding: utf-8 -*-
"""
# @Time    : 2019/8/13 16:49
# @Author  : JW
# @FileName: handle_log.py
"""
import os
import logging
from logging.handlers import RotatingFileHandler  # 处理日志轮转

from common.handle_path import LOGS_DIR


class HandleLog:
    """处理日志类"""

    def __init__(self):
        # 如果不传name参数，那么默认使用root根收集器
        self.case_logger = logging.getLogger("case")
        # 指定日志收集器的日志等级
        self.case_logger.setLevel("DEBUG")
        # 定义日志输出渠道
        console_handle = logging.StreamHandler()
        file_handle = RotatingFileHandler(filename=os.path.join(LOGS_DIR, "cases.log"),
                                          maxBytes=1024 * 1024 * 100,
                                          backupCount=3,
                                          encoding="utf-8")
        # 指定日志输出渠道的日志等级
        console_handle.setLevel("ERROR")
        file_handle.setLevel("INFO")
        # 定义日志显示格式
        verbose_formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(module)s - %(name)s - [日志信息]%(message)s")
        # 设置渠道输出日志的格式
        console_handle.setFormatter(verbose_formatter)
        file_handle.setFormatter(verbose_formatter)
        # 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """获取Logger日志器对象"""
        return self.case_logger


if __name__ == '__main__':
    do_log = HandleLog().get_logger()
    for _ in range(1):
        do_log.debug("这是debug日志")
        do_log.info("这是info日志")
        do_log.warning("这是warning日志")
        do_log.error("这是error日志")
        do_log.critical("这是critical日志")
