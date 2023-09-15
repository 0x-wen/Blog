#import cls_singleton
#
# obj1 = cls_singleton.instance
# print(obj1)
#
# import cls_singleton
#
# obj2 = cls_singleton.instance
# print(obj2)


class Student:
    _instance = None        # 存放实例

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_singleton(cls, name, age):
        if not cls._instance:
            cls._instance = cls(name, age)
        return cls._instance


obj1 = Student.get_singleton("xm", 18)
obj2 = Student.get_singleton("xm", 18)

Student("xm", 18)


print(obj1 is obj2)
