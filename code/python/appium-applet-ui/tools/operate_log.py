
import logging
import os
from logging.handlers import RotatingFileHandler

from tools.constants import LOGS_DIR
from tools.operate_config import do_config


class OperateLog(object):
    """封装处理日志类"""

    def __init__(self):
        self.case_logger = logging.getLogger(do_config("LOG", "logger_name"))
        self.case_logger.setLevel(do_config("LOG", "logger_level"))
        console_handle = logging.StreamHandler()
        file_handle = RotatingFileHandler(filename=os.path.join(LOGS_DIR, do_config("LOG", "log_filename")),
                                          maxBytes=1024 * 1024 * 100,
                                          backupCount=do_config("LOG", "backupCount"),
                                          encoding='utf-8')
        console_handle.setLevel(do_config("LOG", "console_level"))
        file_handle.setLevel(do_config("LOG", "file_level"))

        simple_formatter = logging.Formatter(do_config("LOG", "simple_formatter"))
        verbose_formatter = logging.Formatter(do_config("LOG", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)

        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """获取Logger日志器对象"""
        return self.case_logger


do_log = OperateLog().get_logger()

if __name__ == '__main__':
    for _ in range(1):
        do_log.debug("这是debug日志")
        do_log.info("这是info日志")
        do_log.warning("这是warning日志")
        do_log.error("这是error日志")
        do_log.critical("这是critical日志")
