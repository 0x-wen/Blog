# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 13:59
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User  # 导入Django中的User模型类
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class UsersLoginResponseSerializer(serializers.Serializer):
    """定义user_response返回数据的序列化器"""
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(required=True)


class UsersRegisterModelSerializer(serializers.ModelSerializer):
    """定义user_register序列化器"""

    password = serializers.CharField(label='密码', help_text='密码', write_only=True, min_length=6,
                                     max_length=20, error_messages=
                                     {'min_length': '仅允许输入6-20个字符', 'max_length': '仅允许输入6-20个字符'})
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码', write_only=True, min_length=6,
                                             max_length=20, error_messages=
                                             {'min_length': '仅允许输入6-20个字符', 'max_length': '仅允许输入6-20个字符'})
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirm', 'email', 'token')

        extra_kwargs = {
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'required': True,
                'write_only': True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message="邮箱不能重复")]}
        }

    def validate(self, attrs):
        """5.对多个字段联合校验"""
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('两次输入密码不一致')
        attrs.pop('password_confirm')
        return attrs

    def create(self, validated_data):
        """注册成功之后需要返回token"""
        obj = User.objects.create_user(**validated_data)
        # 创建token
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        obj.token = token
        return obj
