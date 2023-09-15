# -*- coding: utf-8 -*-

class MyClass(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        print("getattr 获取不存在的对象属性时触发")
        # super().__delattr__(item)  # 'MyClass' object has no attribute 'id'
        return self.__dict__.get(item)

    def __setattr__(self, key, value):
        print("setattr 设置修改对象属性时触发")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("delattr 删除对象属性时触发")
        if item == "name":  # 属性是name时抛出异常，或者不进行删除操作
            # raise AttributeError("name 属性不让删除...")
            pass
        else:
            super().__delattr__(item)

    def __getattribute__(self, name):
        # 访问任何属性（包括存在的和不存在的属性）时都会调用 __getattribute__ 方法
        print("__getattribute__ called")
        return super().__getattribute__(name)


a = MyClass("李四", 18)  # 每一次给属性赋值 都会执行setattr方法
print(a.id)
del a.age  # 触发delattr方法
print(f"查看对象属性:{a.__dict__}")
