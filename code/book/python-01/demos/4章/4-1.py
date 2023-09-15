class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"My name id {self.name}")


stu1 = Student("xiaoming", 18)

stu2 = Student("xh", 9)

print(id(stu1))
print(id(stu2))




