# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers

from interfaces.models import Interfaces
from projects.models import Projects
from utils import validators
from .models import Configures


class ProjectInterfaceNameModelSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(label='所属项目名称', help_text='所属项目名称', read_only=True, slug_field='name')

    pid = serializers.IntegerField(label='所属项目ID', write_only=True, validators=[validators.validate_project_id_exist])
    iid = serializers.IntegerField(label='所属接口ID', write_only=True, validators=[validators.validate_interface_id_exist])

    class Meta:
        model = Interfaces
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


class ConfiguresModelSerializer(serializers.ModelSerializer):
    interface = ProjectInterfaceNameModelSerializer(help_text='配置所属项目和接口')

    class Meta:
        model = Configures
        exclude = ('update_time', 'create_time',)

    def to_internal_value(self, data):
        """create 之前要先对数据进行处理"""
        data = super().to_internal_value(data)
        pop_value = data.pop('interface')
        data["interface_id"] = pop_value.get("iid")

        return data


