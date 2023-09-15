# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 13:32
# @Author  : Jw
# @File    : pagination.py
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination as _PageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(_PageNumberPagination):
    """自定义分页传参"""
    # The default page size.
    # Defaults to `None`, meaning pagination is disabled.
    page_size = 10

    # Client can control the page using this query parameter.
    page_query_param = 'page'  # 页号
    page_query_description = 'A page number within the paginated result set.'

    # Client can control the page size using this query parameter.
    # Default is 'None'. Set to eg 'page_size' to enable usage.
    page_size_query_param = 'size'  # 数量
    page_size_query_description = 'Number of results to return per page.'

    # Set to an integer to limit the maximum page size the client may request.
    # Only relevant if 'page_size_query_param' has also been set.
    max_page_size = 100

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        # self 为当前PageNumberPagination对象，中page.number是当前页码数
        # 即在响应的数据中 增加了当前页码数 page = self.page.number
        response.data["current_page_num"] = self.page.number
        response.data['total_pages'] = self.page.paginator.num_pages
        return response
