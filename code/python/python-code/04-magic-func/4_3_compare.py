# -*- coding: utf-8 -*-

class Student:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        print("__eq__ is running ... 可自定义比较逻辑")
        if isinstance(other, Student):
            return self.age == other.age  # 返回布尔值
        return False


print(Student(18) == Student(18))
print(Student(18) != 18)  # nq, 不相等的逻辑。如果没有实现，则默认是eq的结果取反。
print(dir(Student(18)))  # __lt__、__gt__、__le__、__ge__ 分别表示小于、大于、小于等于和大于等于。
