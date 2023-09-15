from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt import authentication

from utils.mixins import NamesMixin
from utils.pagination import PageNumberPagination
from . import serializers
from .models import Envs


class EnvsViewSet(NamesMixin, viewsets.ModelViewSet):
    """
    list: 获取所有接口
    create: 创建接口
    retrieve: 查询某个接口
    update: 修改某个接口
    destroy: 删除某个接口
    partial_update: 部分更新
    """
    queryset = Envs.objects.all()
    serializer_class = serializers.EnvsModelSerializer
    # 这里指定优先级高于全局
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看
    # 设置类视图认证方法,若有其他特殊认证方式在这里指定
    authentication_class = [SessionAuthentication, authentication.JSONWebTokenAuthentication]

    # 增加两个过滤引擎
    filter_backends = [SearchFilter, OrderingFilter]
    # 对哪些字段可以搜索
    search_fields = ['^name', '=tester']
    # 支持哪些字段排序,'__all__' 所有字段都可以排序
    ordering_fields = ['id', 'name']
    # 默认排序字段
    ordering = ['id']
    # page or page_size分页处理 可以在view中指定，优先级大于全局配置
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        """获取不同的序列化器类"""
        if self.action == 'names':
            return serializers.EnvsNamesModelSerializer
        else:
            return super().get_serializer_class()
