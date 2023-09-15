class Student:
    _instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


stu1 = Student("xm")
stu2 = Student("xm")
print(id(stu1), id(stu2))
