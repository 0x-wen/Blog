class MyType(type):

    def __init__(cls, name, bases=None, dict=None):
        super().__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        obj = cls.__new__(cls, *args, **kwargs)
        obj.__init__(*args, **kwargs)
        cls._instance = obj
        return cls._instance


class Student(metaclass=MyType):
    def __init__(self, name):
        self.name = name


stu1 = Student("xm")
stu2 = Student("xm")
print(stu1 is stu2)
print(id(stu1))
print(id(Student._instance))