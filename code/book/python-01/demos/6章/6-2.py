"""
type(name, bases, dict) -> a new type

class Person(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
    pass
"""


def __init__(self, name):
    self.name = name

def talk(self):
    print(f"i am {self.name}")

name = "Person"
bases = (object, )
dict = {"__init__": __init__, "talk": talk}

Person = type(name, bases, dict)
print(Person)

p = Person("xm")
print(p.name)
p.talk()