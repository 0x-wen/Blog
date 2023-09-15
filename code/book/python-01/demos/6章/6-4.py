"""
Person = type(name, bases, dict)
"""


class MyType(type):
    def __init__(cls, name, bases=None, dict=None):
        if not name.istitle():
            raise NameError("类名首字字母必须大写")
        if "__doc__" not in dict:
            raise NameError("必须要有注释")



class People(object, metaclass=MyType):
    pass