# -*- coding: utf-8 -*-
import abc


# 指定metaclass属性将类设置为抽象类，抽象类本身只是用来约束子类的，抽象类本身不能被实例化
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 该装饰器限制子类必须定义有一个名为talk的方法
    def talk(self):  # 抽象方法中无需实现具体的功能
        pass


class Cat(Animal):  # 但凡继承Animal的子类都必须遵循Animal规定的标准
    def talk(self):  # 必须定义talk方法
        pass


cat = Cat()  # 若子类中没有一个定义talk的方法则会抛出异常TypeError，无法实例化
