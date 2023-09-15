# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/5/12 14:46
@file: test_01.py
"""
import unittest
import inspect
import warnings

from libs.ddt import ddt, data
from scripts.handle_request import HttpRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_log import do_log
from scripts.constants import TEST_DATAS_FILE_PATH
from scripts.handle_config import do_config
from scripts.handle_dependence import HandleDependence
from scripts.handle_context import Context


@ddt
class Test01(unittest.TestCase):
    new_excel = HandleExcel.copy_file(TEST_DATAS_FILE_PATH)
    do_excel = HandleExcel(filename=new_excel, sheetname="Sheet1")
    test_data = do_excel.get_cases()

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        cls.send_request = HttpRequest()
        do_log.info('\n{:*^50s}'.format('---开始用例---'))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.send_request.close()
        do_log.info('\n{:*^50s}'.format('---执行结束---'))

    @data(*test_data)
    def test_001(self, data_namedtuple):
        do_log.info('\n当前运行的实例方法名：{}'.format(inspect.stack()[0][3]))

        headers = HandleDependence.num_convert(data=data_namedtuple.headers)
        if data_namedtuple.data:  # 为空会报错
            data = HandleDependence.num_convert(data=Context.parameterization(data_namedtuple.data))
        else:  # 局部变量“data”在赋值之前被引用
            data = HandleDependence.num_convert(data=data_namedtuple.data)

        if data_namedtuple.case_depend:
            # 判断是否有依赖，有数据依赖进行数据拆分
            depend_data = data_namedtuple.dependence
            get_value = HandleDependence.get_value(data=depend_data)
            update_value_tuple = HandleDependence.update_value(data=data_namedtuple.update_value, value=get_value)
            headers_dict = update_value_tuple[0]
            body_dict = update_value_tuple[1]
            headers.update(headers_dict)
            data.update(body_dict)

        response = self.send_request(method=data_namedtuple.method,
                                     url="https://xxxxx.xxxxx.net" + data_namedtuple.url,
                                     data=data,
                                     is_json=True,
                                     headers=headers)

        try:
            self.assertIn(data_namedtuple.expected, response.text, msg='测试【{}】失败'.format(data_namedtuple.title))
        except AssertionError as e:
            do_log.error('异常信息为{}'.format(e))
            Test01.do_excel.write_result(row=data_namedtuple.case_id + 1,
                                         actual=response.text,
                                         result=do_config('MSG', 'fail_result'))
            raise e
        else:
            Test01.do_excel.write_result(row=data_namedtuple.case_id + 1,
                                         actual=response.text,
                                         result=do_config('MSG', 'success_result'))


if __name__ == '__main__':
    unittest.main()
