"""
- 创建一个空对象   __new__
- 初始化空对象    __init__
- 返回初始化完成的对象
"""


class MyType(type):
    def __call__(cls, *args, **kwargs):
        # 1: 创建一个空对象
        obj = cls.__new__(cls, *args, **kwargs)
        print(id(obj))
        # 2: 初始化空对象
        cls.__init__(obj, *args, **kwargs)
        # obj.__init__(*args, **kwargs)

        # 3 返回初始化完成的对象
        return obj


class Student(metaclass=MyType):
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("xm", 18)
print(id(stu))