a = "123"

class People(object):
    pass


class Student(People):
    pass


s = Student()


print(type(s))


print(isinstance(s, (int, str)))

print(issubclass(Student, People))