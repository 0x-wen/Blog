class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"My name id {self.name}")

    def edit_name(this, new_name):
        this.name = new_name

    @classmethod
    def create_student(cls, name, age):
        return cls(name, age)

    @staticmethod
    def hello(name):
        print("12345678")


stu1 = Student("xm", 18)
stu2 = Student("xh", 18)
stu1.say_hello()
stu1.edit_name("x_m")
stu1.say_hello()
stu2.say_hello()

stu3 = Student.create_student("xl", 9)
print(stu3)

stu1.hello("as")
Student.hello("as")

