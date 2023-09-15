# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers

from envs.models import Envs


class EnvsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        exclude = ('update_time',)

        extra_kwargs = {
            'create_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            },
            'validators': {
                'message': '环境名称不能重复'
            },
        }


class EnvsNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name')
        read_only = ('name',)
