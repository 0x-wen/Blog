# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers

from .models import Reports


class ReportsModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reports
        exclude = ('update_time',)

        extra_kwargs = {
            'create_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret.get('result'):
            ret['result'] = 'pass'
        else:
            ret['result'] = 'fail'
        return ret
