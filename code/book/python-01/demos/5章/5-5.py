class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        print("le")
        return self.age <= other.age

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return 1


stu1 = Student("xm", 10)
stu2 = Student("xh", 11)

print(stu1 != stu2)
