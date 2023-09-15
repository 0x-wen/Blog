# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 15:46
# @Author  :  Jw
# @File    : operate_config.py
from configparser import ConfigParser

from tools.constants import TEST_CASES_INI_PATH


class OperateConfig(ConfigParser):
    """定义处理配置文件类"""

    def __init__(self, filename=None):
        super().__init__()
        self.filename = filename

    def __call__(self, section="DEFAULT", option=None, is_eval=False, is_bool=False):
        """
        '对象()'这种形式，__call__方法会被调用
        :param section: 区域名
        :param option: 选项名
        :param is_eval: 为默认参数，是否进行eval函数转换，默认不转换
        :param is_bool: 选项所对应的值是否需要转化为bool类型，默认不转换
        :return:
        """
        self.read(self.filename, encoding="utf-8")
        if option is None:
            return dict(self[section])

        if isinstance(is_bool, bool):
            if is_bool:
                return self.getboolean(section, option)
        else:
            raise ValueError("is_bool必须是布尔类型数据")
        data = self.get(section, option)
        if data.isdigit():
            return int(data)
        try:
            return float(data)
        except ValueError:
            pass

        if isinstance(is_eval, bool):
            if is_eval:
                return eval(data)
        else:
            raise ValueError("is_eval转换数据类型出错")
        return data


do_config = OperateConfig(filename=TEST_CASES_INI_PATH)
if __name__ == '__main__':
    config = OperateConfig(TEST_CASES_INI_PATH)
    print(config("REPORT", "verbosity"), type(config("REPORT", "verbosity")))
