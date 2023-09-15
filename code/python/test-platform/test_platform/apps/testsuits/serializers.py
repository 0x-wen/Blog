# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
import json
import re

from rest_framework import serializers

from interfaces.models import Interfaces
from projects.models import Projects
from utils import validators
from .models import TestSuits


class TestSuitsModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(label='项目ID', queryset=Projects.objects.all())

    class Meta:
        model = TestSuits
        fields = "__all__"

        extra_kwargs = {
            'create_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            },
            'update_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }

    def validate_include(self, value):
        """验证include字段类型是 json中数组类型"""
        result = re.match(r'^\[\d+(, *\d+)*\]$', value)
        if result is None:
            raise serializers.ValidationError('参数格式有误')

        result = result.group()
        try:
            result_dict = json.loads(result)
        except Exception:
            raise serializers.ValidationError('参数格式转化有误')

        for item in result_dict:
            if not Interfaces.objects.filter(pk=item).exists():
                raise serializers.ValidationError(f'接口id:{item},不存在')

        return value

    def to_internal_value(self, data):
        tmp = super().to_internal_value(data)
        tmp["project_id"] = tmp.get('project_id').pk
        # 这里返回data和tmp没有区别,dict是引用对象,即修改完之后的数据 tmp = data (create)
        # 在update时 tmp != data
        return tmp


class TestSuitsRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(label='所属环境ID', validators=[validators.validate_env_id_exist])

    class Meta:
        model = TestSuits
        fields = ('id', 'env_id')
