# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers

from .models import TestCases
from interfaces.models import Interfaces
from utils import validators


class ProjectInterfaceModelSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(label='所属项目名称', help_text='所属项目名称', read_only=True, slug_field='name')
    # 方式一：输出时会设置interface_id为只读，因为根据模型类生成的数据
    # project_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Projects.objects.all())

    # 方式二：自定义pid 和iid
    pid = serializers.IntegerField(label='所属项目ID', write_only=True, validators=[validators.validate_project_id_exist])
    iid = serializers.IntegerField(label='所属接口ID', write_only=True, validators=[validators.validate_interface_id_exist])

    class Meta:
        model = Interfaces
        # fields = ('name', 'id', 'project', 'project_id')
        fields = ('name', 'iid', 'project', 'pid')

        extra_kwargs = {
            'name': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        """多个字段联合校验"""
        # 判断项目pid中是否存在iid 这个模型类只是用于输出展示的，创建用例的时候并不需要pid 和 iid
        pid = attrs.get('pid')
        iid = attrs.get('iid')
        if not Interfaces.objects.filter(pk=iid, project_id=pid).exists():
            raise serializers.ValidationError('所属项目ID和接口ID不匹配')
        return attrs


class TestCasesModelSerializer(serializers.ModelSerializer):
    interface = ProjectInterfaceModelSerializer(help_text='用例所属接口和项目')

    class Meta:
        model = TestCases
        exclude = ('update_time', 'create_time',)

        extra_kwargs = {
            'request': {
                'write_only': True
            },
            'setup': {
                'write_only': True
            }
        }

    def to_internal_value(self, data):
        # 创建用例的数据，interface需要更改
        data = super().to_internal_value(data)
        pop_value = data.pop('interface')
        data['interface_id'] = pop_value.get('iid')
        return data


class TestCaseRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(label='所属环境ID', validators=[validators.validate_env_id_exist])

    class Meta:
        model = TestCases
        fields = ('id', 'env_id')
