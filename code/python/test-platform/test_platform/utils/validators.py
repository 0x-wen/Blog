# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 16:07
# @Author  : Jw
# @File    : validators.py
from rest_framework import serializers
from projects.models import Projects
from interfaces.models import Interfaces
from envs.models import Envs


def validate_project_id_exist(value):
    """
    3.自定义校验方法  * validators=[validate_project_id_exist]
    校验失败：必须抛出一个 ValidationError 异常
    """
    if not Projects.objects.filter(pk=value).exists():
        raise serializers.ValidationError('项目ID不存在')


def validate_interface_id_exist(value):
    if not Interfaces.objects.filter(pk=value).exists():
        raise serializers.ValidationError('接口ID不存在')


def validate_env_id_exist(value):
    if not Envs.objects.filter(pk=value).exists():
        raise serializers.ValidationError('环境管理ID不存在')
