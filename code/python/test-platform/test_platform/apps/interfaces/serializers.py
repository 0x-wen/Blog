# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers
from rest_framework.response import Response

from configures.models import Configures
from interfaces.models import Interfaces
from projects.models import Projects
from testcases.models import TestCases
from utils import validators


class InterfacesModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(label='项目ID', queryset=Projects.objects.all())

    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester', 'project', 'create_time', 'project_id', 'desc')

        extra_kwargs = {
            'create_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }

    def to_internal_value(self, data):
        # TODO 检查前端传入data中的项目ID 是数字还是模型对象  -- 已完成
        tmp = super().to_internal_value(data)
        tmp["project_id"] = tmp.get('project_id').pk
        # 这里返回data和tmp没有区别,dict是引用对象,即修改完之后的数据 tmp = data (create)
        # 在update时 tmp != data
        return tmp


class ConfiguresSerializerDAB(serializers.ModelSerializer):
    class Meta:
        model = Configures
        fields = ('id', 'name')


class ConfigNamesSerializer(serializers.ModelSerializer):
    configures = ConfiguresSerializerDAB(label='接口所属配置信息', help_text='接口所属配置信息', read_only=True, many=True)

    class Meta:
        model = Interfaces
        fields = ('configures',)


class TestCasesSerializerDAB(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = ('id', 'name')


class TestCasesNamesSerializer(serializers.ModelSerializer):
    testcases = TestCasesSerializerDAB(label='接口所属用例信息', help_text='接口所属用例信息', read_only=True, many=True)

    class Meta:
        model = Interfaces
        fields = ('testcases',)


class InterfaceRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(label='所属环境ID', validators=[validators.validate_env_id_exist])

    class Meta:
        model = Interfaces
        fields = ('id', 'env_id')
