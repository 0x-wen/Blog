import json
import os
from datetime import datetime

from django.conf import settings
from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework import generics, mixins, permissions
from rest_framework import authentication as _authentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_jwt import authentication

from envs.models import Envs
from interfaces.models import Interfaces
from testcases.models import TestCases
from testsuits.models import TestSuits
from utils import common
from utils.pagination import PageNumberPagination
from . import serializers


class TestSuitsViewSet(viewsets.ModelViewSet):
    """
    list: 获取所有接口
    create: 创建接口
    retrieve: 查询某个接口
    update: 修改某个接口
    destroy: 删除某个接口
    partial_update: 部分更新
    """
    queryset = TestSuits.objects.all()
    serializer_class = serializers.TestSuitsModelSerializer
    # 这里指定优先级高于全局
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看
    # 设置类视图认证方法,若有其他特殊认证方式在这里指定
    authentication_class = [_authentication.SessionAuthentication, authentication.JSONWebTokenAuthentication]

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

    @action(methods=['post'], detail=True, )
    def run(self, request, *args, **kwargs):
        """执行测试用例接口"""
        # 1.获取项目模型对象并获取env_id
        instance = self.get_object()  # type:TestSuits

        # 方式二：调用创建 不保存数据即可,改造perform_create
        res = self.create(request, *args, **kwargs)

        env = Envs.objects.get(pk=res.data.get('env_id'))

        # 2.创建一个以时间戳命名的项目目录
        suites_dir = os.path.join(settings.SUITES_PATH, datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))
        os.mkdir(suites_dir)

        # +获取当前套件中的接口数据
        try:
            interface_id_list = json.loads(instance.include)
        except Exception as e:
            data = {'result': False,
                    'msg': '此套件下include参数有误!'}
            print(f'转换include参数错误:{e}')
            return Response(data=data, status=400)
        if interface_id_list is None:
            data = {'result': False,
                    'msg': '此套件没有接口信息,无法运行!'}
            return Response(data=data, status=400)

        # +获得条件下的 每个接口用例数据
        need_run_testcases = list()
        for interface_id in interface_id_list:
            testcases_qs = TestCases.objects.filter(interface_id=interface_id)
            if not testcases_qs.exists():
                continue
            else:
                need_run_testcases.extend(list(testcases_qs))

        # need_run_testcases 判断需要执行的list是否为空
        if len(need_run_testcases) == 0:
            data = {'result': False,
                    'msg': '此套件下没有用例，无法运行！'}
            return Response(data=data, status=400)

        for testcase_obj in need_run_testcases:
            # 3.创建以接口命名的目录/创建yaml用例文件
            common.generate_testcase_file(testcase_obj, env, suites_dir)

        # 4.运行用例并生成报告
        return common.run_testcase(instance, suites_dir)

    def get_serializer_class(self):
        """获取不同的序列化器类"""
        if self.action == 'run':
            return serializers.TestSuitsRunSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        if self.action == "run":
            return
        else:
            super().perform_create(serializer)
