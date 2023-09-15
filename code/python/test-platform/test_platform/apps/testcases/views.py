import json
import logging
import os
from datetime import datetime

from django.conf import settings
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets

from envs.models import Envs
from utils import handle_data, common

from .models import TestCases
from . import serializers
from utils.pagination import PageNumberPagination

logger = logging.getLogger('django')


class TestCasesViewSet(viewsets.ModelViewSet):
    """
    list: 获取所有用例
    create: 创建用例
    retrieve: 查询某个用例
    update: 修改某个用例
    destroy: 删除某个用例
    partial_update: 部分更新
    """
    queryset = TestCases.objects.all()
    serializer_class = serializers.TestCasesModelSerializer
    # 这里指定优先级高于全局
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看
    # 增加两个过滤引擎
    filter_backends = [SearchFilter, OrderingFilter]
    # 对哪些字段可以搜索
    search_fields = ['^name', '=id']
    # 支持哪些字段排序,'__all__' 所有字段都可以排序
    ordering_fields = ['id', 'name']
    # 默认排序字段
    ordering = ['id']
    # page or page_size分页处理 可以在view中指定，优先级大于全局配置
    pagination_class = PageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        testcase_obj = self.get_object()  # type:TestCases

        # 获取model中的setup字段信息，里面包含了 配置信息和关联用例
        try:
            testcase_setup = json.loads(testcase_obj.setup)
        except Exception as e:
            testcase_setup = dict()

        # 获取当前用例的请求参数
        try:
            testcase_request = json.loads(testcase_obj.request)
        except Exception as e:
            err = {'msg': '请求参数有误', 'status': 0}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        testcase_request_data = testcase_request.get('test').get('request')
        testcase_extract = testcase_request.get('test').get("extract")
        testcase_parameter = testcase_request.get('test').get("parameters")
        testcase_setup_hooks = testcase_request.get('test').get("setup_hooks")
        testcase_teardown_hooks = testcase_request.get('test').get("teardown_hooks")
        testcase_validate = testcase_request.get('test').get("validate")
        testcase_variable = testcase_request.get('test').get("variables")

        data = {
            "author": testcase_obj.author,
            "testcase_name": testcase_obj.name,
            "selected_configure_id": testcase_setup.get('config'),
            "selected_interface_id": testcase_obj.interface_id,
            "selected_project_id": testcase_obj.interface.project_id,
            # 测试用例前置 接口
            "selected_testcase_id": testcase_setup.get('testcases') or [],
            "method": testcase_request_data.get('method') or 'GET',
            "url": testcase_request_data.get('url'),
            "params": handle_data.handle_data4(testcase_request_data.get("params")),
            "headers": handle_data.handle_data4(testcase_request.get('headers')),
            # 表单参数
            "variable": handle_data.handle_data2(testcase_request_data.get("data")),
            # json 以json格式传递数据
            "jsonVariable": json.dumps(testcase_request_data.get("json")),
            # 提取
            "extract": handle_data.handle_data3(testcase_extract),
            "validate": handle_data.handle_data1(testcase_validate),

            "globalVar": handle_data.handle_data2(testcase_variable),
            "parameterized": handle_data.handle_data3(testcase_parameter),
            "setupHooks": handle_data.handle_data5(testcase_setup_hooks),
            "teardownHooks": handle_data.handle_data5(testcase_teardown_hooks),
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, )
    def run(self, request, *args, **kwargs):
        """执行测试用例接口"""
        # 1.获取用例模型对象并获取env_id
        instance = self.get_object()
        # 方式一：因为testcase、model中没有env_id
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # env_id = serializer.validated_data.get('env_id')

        # 方式二：调用创建 不保存数据即可,改造perform_create
        res = self.create(request, *args, **kwargs)

        env = Envs.objects.get(pk=res.data.get('env_id'))

        # 2.创建一个以项目命名的目录
        suites_dir = os.path.join(settings.SUITES_PATH, datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))
        os.mkdir(suites_dir)
        # 3.创建以接口命名的目录/创建yaml用例文件
        common.generate_testcase_file(instance, env, suites_dir)
        # 4.运行用例并生成报告

        return common.run_testcase(instance, suites_dir)
        pass

    def get_serializer_class(self):
        return serializers.TestCaseRunSerializer if self.action == "run" else super().get_serializer_class()

    def perform_create(self, serializer):
        if self.action == "run":
            return
        else:
            super().perform_create(serializer)
