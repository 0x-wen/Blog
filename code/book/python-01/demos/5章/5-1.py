class Student:
    def __init__(self, name, age):
        print("init...")
        self.name = name
        self.age = age

    def __del__(self):
        print("del...")


stu = Student("xm", 18)
print(stu.name, stu.age)

# del stu     # 手动回收对象stu


