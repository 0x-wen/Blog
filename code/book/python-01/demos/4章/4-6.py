class Student:
    school = "PKU"

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("xm", 18)
stu.school = "xwxx"
print(stu.__dict__)
print(stu.__dict__["name"])

print(stu.name)
print(stu.age)
print(stu.school)
