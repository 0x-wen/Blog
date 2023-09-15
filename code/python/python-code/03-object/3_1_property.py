# -*- coding: utf-8 -*-

# 面向对象三大特性：继承 封装 多态
class Base(object):
    def __init__(self):
        self.leg = "4"

    def func1(self):
        print(f"Base 有 {self.leg} 条腿...")


class Cat(Base):
    def func1(self):
        print(f"我是cat,有{self.leg}条腿...")
        print("我会上树")


class Dog(Base):
    def func1(self):
        print(f"我是dog,有{self.leg}条腿...")
        print("我跑得快")


class Table(Base):
    def func1(self):
        print(f"我是一个餐桌，也有{self.leg}条腿，但我不会跑...")


def func(arg):
    arg.func1()


func(Base())
func(Dog())
func(Cat())
func(Table())
