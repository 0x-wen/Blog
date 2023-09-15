class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say_hello(self):
        print(f"My name is {self.name}")


class Student(People):
    def __init__(self, name, age, sex, code, course):
        super().__init__(name, age, sex)
        self.code = code
        self.course = course


class Course:
    def __init__(self, name):
        self.name = name


c = Course("语文")

s = Student("xm", 18, "男", 10111011, c)
s.say_hello()
print(s.course.name)
