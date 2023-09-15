import json

from django.http import FileResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt import authentication

from utils.pagination import PageNumberPagination
from . import serializers
from .models import Reports


class ReportsViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Reports.objects.all()
    serializer_class = serializers.ReportsModelSerializer
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
        """打开某个报告"""
        response = super().retrieve(request, *args, **kwargs)
        try:
            response.data['summary'] = json.loads(response.data.get('summary'))
        except Exception as e:
            raise e
        return response

    @action(methods=['get'], detail=True)
    def download(self, request, *args, **kwargs):
        """下载报告"""
        instance = self.get_object()  # type:Reports

        # 将instance.html是源码字符串，转换为一个可迭代对象
        response = StreamingHttpResponse(iter(instance.html))

        # 需要添加相关的响应头参数，浏览器才会当做文件下载
        # Content-Type:application/octet-stream
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; charset=UTF-8'
        return response
