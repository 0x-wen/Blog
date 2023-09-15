class Student:
    def __init__(self, name, age):
        print("init...")
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("call...")
        print(sum(args))


stu = Student("xm", 18)
stu(1, 2)

