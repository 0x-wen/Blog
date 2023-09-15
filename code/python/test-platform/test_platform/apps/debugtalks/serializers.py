# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers

from .models import DebugTalks


class DebugTalksModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DebugTalks
        exclude = ('update_time', 'create_time', )

        extra_kwargs = {
        }

