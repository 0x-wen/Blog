import logging
import os
from datetime import datetime

from django.conf import settings
from django.db.models import Count, QuerySet
from rest_framework import generics, mixins, permissions
from rest_framework import authentication as _authentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_jwt import authentication

from configures.models import Configures
from envs.models import Envs
from interfaces.models import Interfaces
from testcases.models import TestCases
from testsuits.models import TestSuits
from utils import common
from utils.mixins import NamesMixin
from .models import Projects
from . import serializers
from utils.pagination import PageNumberPagination

logger = logging.getLogger('django')


class ProjectsViewSet(NamesMixin, viewsets.ModelViewSet):
    """
    list: 获取所有项目
    create: 创建项目
    retrieve: 查询某个项目
    update: 修改某个项目
    destroy: 删除某个项目
    partial_update: 部分更新
    """
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    # 这里指定优先级高于全局
    permission_class = [permissions.IsAuthenticated]  # 设置这个视图类,只有登录了才有权限查看
    # 设置类视图认证方法,若有其他特殊认证方式在这里指定
    authentication_class = [_authentication.SessionAuthentication, authentication.JSONWebTokenAuthentication]

    # 增加两个过滤引擎
    filter_backends = [SearchFilter, OrderingFilter]
    # 对哪些字段可以搜索
    search_fields = ['^name', '=leader']
    # 支持哪些字段排序,'__all__' 所有字段都可以排序
    ordering_fields = ['id', 'name']
    # 默认排序字段
    ordering = ['id']
    # page or page_size分页处理 可以在view中指定，优先级大于全局配置
    pagination_class = PageNumberPagination

    def list(self, *args, **kwargs):
        response = super().list(self, *args, **kwargs)
        for item in response.data['results']:
            # TODO 优化 使用value().annotate()  --已完成
            test_cases_count = 0
            configures_count = 0
            # 当前项目下所属接口
            interfaces_queryset = Interfaces.objects.filter(project_id=item.get('id'))
            interface_testcase_qs = interfaces_queryset.values('id').annotate(Count('testcases'))
            for i in interface_testcase_qs:
                test_cases_count += i.get('testcases__count')
            interface_config_qs = interfaces_queryset.values('id').annotate(Count('configures'))
            for i in interface_config_qs:
                configures_count += i.get('configures__count')
            # interface_qs = Interfaces.objects.filter(project_id=item.get('id'))
            # for qs in interface_qs:
            #     test_cases_count += TestCases.objects.filter(interface_id=qs.id).count()
            #     configures_count += Configures.objects.filter(interface_id=qs.id).count()
            item["interfaces"] = interfaces_queryset.count()
            item['testsuits'] = TestSuits.objects.filter(project_id=item.get('id')).count()
            item['testcases'] = test_cases_count
            item['configures'] = configures_count
        return response

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        """查询某个项目下的接口信息"""
        res = super().retrieve(request, *args, **kwargs)
        res.data = res.data.get('interfaces')
        return res

    @action(methods=['post'], detail=True, )
    def run(self, request, *args, **kwargs):
        """执行测试用例接口"""
        # 1.获取项目模型对象并获取env_id
        instance = self.get_object()

        # 方式二：调用创建 不保存数据即可,改造perform_create
        res = self.create(request, *args, **kwargs)

        env = Envs.objects.get(pk=res.data.get('env_id'))

        # 2.创建一个以时间戳命名的项目目录
        suites_dir = os.path.join(settings.SUITES_PATH, datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))
        os.mkdir(suites_dir)

        # +获取当前项目的接口数据
        interface_qs = Interfaces.objects.filter(project=instance)
        interface_qs: QuerySet
        if not interface_qs.exists():
            data = {'result': False,
                    'msg': '此项目下没有接口，无法运行！'}
            return Response(data=data, status=400)

        # +获得每个接口下的用例数据
        need_run_testcases = list()
        for interface_obj in interface_qs:
            testcases_qs = TestCases.objects.filter(interface=interface_obj)
            if not testcases_qs.exists():
                continue
            else:
                need_run_testcases.extend(list(testcases_qs))

        # need_run_testcases 判断需要执行的list是否为空
        if len(need_run_testcases) == 0:
            data = {'result': False,
                    'msg': '此项目下没有用例，无法运行！'}
            return Response(data=data, status=400)

        for testcase_obj in need_run_testcases:
            # 3.创建以接口命名的目录/创建yaml用例文件
            common.generate_testcase_file(testcase_obj, env, suites_dir)

        # 4.运行用例并生成报告
        return common.run_testcase(instance, suites_dir)

    def get_serializer_class(self):
        """获取不同的序列化器类"""
        if self.action == 'names':
            return serializers.ProjectsNamesModelSerializer
        elif self.action == 'interfaces':
            return serializers.InterfacesNamesModelSerializer
        elif self.action == 'run':
            return serializers.ProjectRunSerializer
        else:
            return super().get_serializer_class()

    def perform_create(self, serializer):
        if self.action == "run":
            return
        else:
            super().perform_create(serializer)
