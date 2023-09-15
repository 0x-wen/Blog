# -*- coding: utf-8 -*-
"""
@author: jw
@time: 2020/5/13 14:04
@file: handle_dependence.py
"""
from scripts.handle_excel import HandleExcel
from scripts.handle_request import HttpRequest
from scripts.constants import TEST_DATAS_FILE_PATH
import json
import jsonpath
from scripts.handle_request import do_log
from scripts.handle_context import Context


class HandleDependence:
    """定义处理接口关联的类"""

    @staticmethod
    def get_value(data):
        """
        :param data: 接口按规则入参数据
        :return: 返回一个两个字典数据
        """
        depend_list = data.split(";")
        new_value_list = []

        for i in depend_list:
            one_data = i.split("|")
            int_id = int(one_data[0])
            request_id = int_id + 1
            t1_excel_obj = HandleExcel(filename=TEST_DATAS_FILE_PATH, sheetname="Sheet1").get_case(request_id)[0]

            # 进行数据请求
            if t1_excel_obj.case_depend:
                # 如果有多个依赖请求的时候，先取出原headers和原body，更新之后再去请求
                headers = HandleDependence.num_convert(data=t1_excel_obj.headers)
                # 有值将请求数据进行参数化，无值要返回data
                if t1_excel_obj.data:
                    data = HandleDependence.num_convert(data=Context.parameterization(t1_excel_obj.data))
                else:
                    data = HandleDependence.num_convert(data=t1_excel_obj.data)

                update_value_tuple = HandleDependence.update_value(data=t1_excel_obj.update_value, value=new_value_list)
                headers_dict = update_value_tuple[0]
                body_dict = update_value_tuple[1]
                headers.update(headers_dict)
                data.update(body_dict)

                one_res = HttpRequest()(method=t1_excel_obj.method,
                                        url="https://xxxxxx.net" + t1_excel_obj.url,
                                        data=data,
                                        is_json=True,
                                        headers=headers)
            else:
                one_res = HttpRequest()(method=t1_excel_obj.method,
                                        url="https://xxxx.net" + t1_excel_obj.url,
                                        data=HandleDependence.num_convert(t1_excel_obj.data),
                                        is_json=True)

            one_value = json.loads(one_data[1])
            # 判断要取的值中是否有response，如果有将去响应中取出list中的所有值
            if "response" in one_value:
                respone_list_vlaue = one_value["response"]
                if respone_list_vlaue:
                    dict_1 = {}
                    for j in respone_list_vlaue:
                        key = j.split(".")[-1]
                        value = jsonpath.jsonpath(one_res.json(), expr=j)
                        dict_1[key] = value[0]
                    new_value_list.append(dict_1)
            if "headers" in one_value:
                headers_list_vlaue = one_value["headers"]
                if headers_list_vlaue:
                    dict_1 = {}
                    for k in headers_list_vlaue:
                        value = one_res.headers[k]
                        dict_1[k] = value
                    new_value_list.append(dict_1)
        return new_value_list

    @staticmethod
    def update_value(data, value):
        """更新请求值，返回两个字典，headers和body"""
        if isinstance(data, str):
            data = json.loads(data)
        headers_dict = {}
        body_dict = {}
        if "headers" in data:
            for i in data["headers"]:
                for j in value:
                    if i in j:
                        headers_dict[i] = j[i]

        if "body" in data:
            for i in data["body"]:
                for j in value:
                    if i in j:
                        body_dict[i] = j[i]
        return headers_dict, body_dict

    @staticmethod
    def num_convert(data):
        if data:
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except Exception as e:
                    do_log.error("将数据转换为字典类型时出现异常{}".format(e))
                    data = eval(data)
        else:
            data = {}
        return data


if __name__ == '__main__':
    str_1 = '1|{"response":["$.data.token"],"headers":["Content-Type"]};2|{"response":["$.data.size"]}'
    str_2 = {"headers": ["token", "Content-Type"], "body": ["size"]}
    a = HandleDependence().get_value(data=str_1)
    print(a)
    print(HandleDependence().update_value(data=str_2, value=a))
    pass
