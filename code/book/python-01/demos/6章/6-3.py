class Mytype(type):
    pass


class Person(object, metaclass=Mytype):
    def __init__(self, name):
        self.name = name


print(type(Person))