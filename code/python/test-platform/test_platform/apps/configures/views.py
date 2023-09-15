import json

from django.http import FileResponse
from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, mixins, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_jwt import authentication

from interfaces.models import Interfaces
from utils import handle_data
from utils.pagination import PageNumberPagination
from . import serializers
from .models import Configures


class ConfiguresViewSet(viewsets.ModelViewSet):
    queryset = Configures.objects.all()
    serializer_class = serializers.ConfiguresModelSerializer
    # 这里指定优先级高于全局
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看
    # 设置类视图认证方法,若有其他特殊认证方式在这里指定
    authentication_class = [SessionAuthentication, authentication.JSONWebTokenAuthentication]

    # 增加两个过滤引擎
    filter_backends = [SearchFilter, OrderingFilter]
    # 对哪些字段可以搜索
    search_fields = ['^name', ]
    # 支持哪些字段排序,'__all__' 所有字段都可以排序
    ordering_fields = ['id', 'name']
    # 默认排序字段
    ordering = ['id']
    # page or page_size分页处理 可以在view中指定，优先级大于全局配置
    pagination_class = PageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        config_obj = self.get_object()  # type:Configures

        # 获取当前配置中的请求参数
        try:
            config_request = json.loads(config_obj.request)
        except Exception as e:
            err = {'msg': '请求参数有误', 'status': 0}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)
        # 处理请求头数据
        config_headers = config_request['config']['request']['headers']
        config_headers_list = handle_data.handle_data4(config_headers)

        # 处理全局变量数据
        config_variables = config_request['config'].get('variables')
        config_variables_list = handle_data.handle_data2(config_variables)

        config_name = config_request['config']['name']

        selected_interface_id = config_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id

        data = {
            "author": config_obj.author,
            "configure_name": config_name,
            "selected_interface_id": selected_interface_id,
            "selected_project_id": selected_project_id,
            "headers": config_headers_list,
            "globalVar": config_variables_list,
        }
        return Response(data, status=status.HTTP_201_CREATED)
