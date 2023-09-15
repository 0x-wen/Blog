class PkuPeople:
    school = "PKU"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

print(PkuPeople.mro())


class Student(PkuPeople):
    def select_course(self):
        print(f'学生：{self.name}正在选课。。。')


stu = Student("xm", 18, 0)
stu.__dict__


class Teacher(PkuPeople):
    def __init__(self, name, age, sex, level):
        super().__init__(name, age, sex)
        self.level = level

    def score(self):
        print(f'老师：{self.name}正在打分。。。')


print(Teacher.mro())