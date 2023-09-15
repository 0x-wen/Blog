# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:06
# @Author  : Jw
# @File    : serializers.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator  # 2.validators=[系统自带的校验类]

from debugtalks.models import DebugTalks
from interfaces.models import Interfaces
from projects.models import Projects
from utils import validators


def about_django(value):
    """
    3.自定义校验方法  * validators=[about_django]
    校验失败：必须抛出一个 ValidationError 异常
    """
    if '1' not in value.lower():
        raise serializers.ValidationError("项目名称没有包含1")


class MyInterSerializer(serializers.Serializer):
    """自定义序列化器类"""
    id = serializers.IntegerField()
    name = serializers.CharField()
    tester = serializers.CharField()


class ProjectSerializer(serializers.Serializer):
    """
    项目数据序列化器
    默认定义哪些字段,哪些字段就会序列化输出
    """

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=50, min_length=2,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message="项目名称不能重复"),
                                             about_django])
    leader = serializers.CharField(label='项目负责人', help_text='项目负责人', max_length=20, min_length=3, allow_null=True,
                                   error_messages={'min_length': "项目名称不能少于3位",
                                                   'max_length': "项目名称不能超过20位",
                                                   "required": "该字段不能为空"})
    developer = serializers.CharField(label='开发人员', help_text='开发人员', max_length=20,
                                      required=False, allow_blank=True, allow_null=True)
    tester = serializers.CharField(label='测试人员', help_text='测试人员', max_length=20,
                                   required=False, allow_blank=True, allow_null=True)
    desc = serializers.CharField(label='项目描述', help_text='项目描述', default='')
    create_time = serializers.DateTimeField(label='创建时间', help_text='创建时间', required=False,
                                            format='%Y-%m-%d %H:%M:%S')

    # is_build = serializers.BooleanField(label='是否构建', help_text='是否构建', default=False)
    # update_time = serializers.DateTimeField(label='修改时间', help_text='修改时间', required=False,
    #                                         format='%Y-%m-%d %H:%M:%S')

    # 接受一个自定义的序列化器内，来指定从表需要 序列化输出的值
    interfaces = MyInterSerializer(label='接口信息', help_text='接口信息', read_only=True, many=True)
    # 可以给创建的模型类添加动态字段，必须要定义对应的序列化器字段
    token = serializers.CharField(label='token', help_text='token', read_only=True)
    # 处理一些前端必传,后端又不需要存储的数据库的字段信息
    email = serializers.EmailField(write_only=True)

    # 1.输出关联ID
    # interfaces = serializers.PrimaryKeyRelatedField(label='所属接口ID', help_text='所属接口ID', read_only=True, many=True)
    # 2.关联模型__str__  多个结果 many=True
    # interface = serializers.StringRelatedField(label='', help_text='', read_only=True, many=True)

    # 3.关联模型类中指定字段,若需要反序列化输入，必须指定唯一约束字段
    # interface = serializers.SlugRelatedField(label='', help_text='', many=True,
    #                                          slug='name', queryset=Interfaces.objects.all())

    # 4.关联 模型序列化器 or 自定义序列化器
    # interface = InterfacesSerializer()

    """
    # 1.查询出一个模型类对象
    one_project = Projects.objects.filter(pk__in=[1, 3, 5])

    # 2.使用序列化器类 构造一个序列化器对象
    one_serializer = ProjectsSerializer(instance=one_project, many=True)

    # 3.获取序列化数据 通过data属性可以获取序列化后的数据
    serializer_data = one_serializer.data
    # 4.如果要被序列化的是包含多条数据的查询集QuerySet，可以通过添加many=True参数补充说明
    pass
    """

    def validate_name(self, value):
        """4.对单一字段进行验证"""
        if not value.endswith('项目'):
            raise serializers.ValidationError("项目名称必须以'项目'结尾")
        return value

    def validate(self, attrs):
        """5.对多个字段联合校验"""
        name = attrs['name']
        desc = attrs['desc']
        if not desc:
            raise serializers.ValidationError('项目描述不能为空')
        else:
            attrs['tester'] = name + desc
        return attrs

    def to_internal_value(self, data):
        """
        数据校验顺序：1.调用父类to_internal_value方法 -》2.字段类型(bool抛出异常) - 3.字段通用约束 - 4.依次进行validators列表校验
        - 5.validate_单字段名校验 - 6.调用父类to_internal_value方法 -》 7.validate多字段校验
        """
        some_data = super().to_internal_value(data)
        some_data['leader'] = some_data['leader'].upper()
        return some_data

    def to_representation(self, instance):
        """输出序列化数据之前调用此方法，需要return one_obj_data，否则全部是None，前端展示为null"""
        one_obj_data = super().to_representation(instance)
        return one_obj_data

    def create(self, validate_data: dict):
        """
        新建数据  * 执行到这里的数据都是校验通过的数据
        需要在view中 使用serializer 调用save()方法,才会调转过来。
        为什么要这么做？封装所有接口 对于 数据库的操作，不展示在view中 复用性好
        """
        # 校验通过才会执行到这里 使用validated_data获取校验通过的数据
        # one_project = Projects.objects.create(**serializer.validated_data)
        validate_data.pop('user')
        validate_data.pop('email')
        obj = Projects.objects.create(**validate_data)
        obj.token = 'xx-xx-xx'  # 给模型类添加的动态属性
        return obj

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        # one_project.name = project_dict.get('name')
        # one_project.leader = project_dict.get('leader')
        # one_project.is_build = project_dict.get('is_build')
        # one_project.save()

        instance.name = validated_data.get('name', instance.name) or instance.name
        instance.leader = validated_data.get('leader', instance.leader) or instance.leader
        instance.is_build = validated_data.get('is_build', instance.is_build) or instance.is_build
        instance.desc = validated_data.get('desc', instance.desc) or instance.desc
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    """
    模型序列化器类
    1.必须指定model = 模型类
    2.默认实现了create, update方法
    3.会给模型类中 主键，创建时间，修改时间等 read_only=True
    4.模型类中有default 即 required=False
    5.有null=True, blank=True 即 allow_blank=True, allow_null=True
    6.name等添加了唯一标识的，会自动添加系统校验方法 validators=[<UniqueValidator(queryset=Projects.objects.all())>]
    """

    # 如果添加了一个模型类中没有的字段信息，要将字段名称添加至 fields=()中，若 fields = '__all__' or exclude 指定字段则不用

    class Meta:
        model = Projects
        # fields = '__all__'  # 序列化输出所有字段信息
        # fields = ('id', 'name', 'leader')  # 输出指定字段
        exclude = ('update_time',)  # 排除序列化输出字段

        # 哪些字段只想 序列化输出，可以将字段名称填入
        # read_only_fields = ('is_build', 'tester')

        extra_kwargs = {
            'create_time': {
                'format': '%Y-%m-%d %H:%M:%S'
            }
        }

    def create(self, validated_data):
        """创建项目"""
        # validated_data.pop('user')  serializer.save(user={'name':'张三'})
        instance = super().create(validated_data)
        # 业务需求：创建项目之后 需要创建一条debugtalk数据
        DebugTalks.objects.create(project_id=instance.id)
        return instance

    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        return obj


class ProjectsNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')  # 输出指定字段


class InterfacesNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class InterfacesNamesModelSerializer(serializers.ModelSerializer):
    # 想要输出接口表中的id和name,projects模型类中没有这个字段，所以自定义
    interfaces = InterfacesNamesSerializer(label='项目所属接口信息', help_text='项目所属接口信息', read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('interfaces',)


class ProjectRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(label='所属环境ID', validators=[validators.validate_env_id_exist])

    class Meta:
        model = Projects
        fields = ('id', 'env_id')
