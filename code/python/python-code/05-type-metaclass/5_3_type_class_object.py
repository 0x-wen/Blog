# -*- coding: utf-8 -*-
"""
通过type创建类,通过class实例化对象
type -> class -> object
stu1 = MyType() 实例化得到一个类
stu1() 类+() 会调用元类中的 __call__方法,返回一个对象
obj1() 对象+() 会调用类中的 __call__方法
"""


class MyType(type):

    def __init__(cls, what, bases=None, dict=None):
        """
        - 第一步：**获取类名**：class_name = Student
        - 第二步：**获取基类们**：class_bases = (object, )
        - 第三步：**获取类的名称空间**：`class_dict = {"__init__": __init__, ""talk: talk}`
        - 第四步：**调用元类 type实例化产生Student类这个对象**
        """
        super().__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        # 1.创建对象
        obj = cls.__new__(cls, *args, **kwargs)
        # 2.初始化对象
        cls.__init__(obj, *args, **kwargs)  # 等价于: obj.__init__(*args, **kwargs)
        return obj


def __init__(self, name):
    self.name = name


def talk(self):
    return f"{self.name},会唱歌..."


def __call__(self):
    return f"self.name={self.name}, obj1()调用了__call__方法"


class_name = "Student"
class_bases = (object,)
class_dict = {"__init__": __init__, "talk": talk, "__call__": __call__}

stu1 = MyType(class_name, class_bases, class_dict)
print(stu1)  # <class '__main__.Student'>

obj1 = stu1("小明")
print(obj1)
print(obj1.talk())
print(obj1())
