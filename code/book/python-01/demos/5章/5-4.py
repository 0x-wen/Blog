# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print("str..")
#         return f"name: {self.name}, age: {self.age}"
#
#     def __repr__(self):
#         print("repr..")
#         return f"name: {self.name}, age: {self.age}"
#
#
# stu = Student("xm", 18)
# print(stu)



from objprint import objprint


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("jack", 10)
print(stu)
objprint(stu)