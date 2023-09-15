class Foo:
    __x = 1

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __f1(self):
        print("__f1")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("")
        self.__name = value


# # print(Foo.__x)

# print(Foo.__dict__)
#
# print(Foo._Foo__x)

# foo = Foo("xm", 18)
# print(foo.__dict__)
# # print(dir(foo))
# # print(foo._Foo__name)
# # foo._Foo__f1()
#
# foo.__as = 10
# print(foo.__as)

foo = Foo("xm", 18)
foo.name = [1, 2, 3]
print(foo.name)




