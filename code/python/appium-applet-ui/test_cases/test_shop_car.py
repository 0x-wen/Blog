# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 14:57
# @Author  :  Jw
# @File    : test_shop_car.py
import unittest

from libs.ddt import data, ddt


class ParameterTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameterTestCase, self).__init__(methodName)
        global parames
        parames = parame


@ddt
class TestAdd(ParameterTestCase):
    all_data = [{"a": 1, "b": 2}, {"a": 2, "b": 2}]

    @data(*all_data)
    def test_add(self, one_data):
        a = one_data["a"] + one_data["b"]
        # print(a)


if __name__ == '__main__':
    unittest.main()
