class People:
    def __init__(self, name, w, h):
        self.__name = name
        self.w = w
        self.h = h

    @property
    def bmi(self):
        return self.w / (self.h ** 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise ValueError("只能使用字符串")
        self.__name = value

    @name.deleter
    def name(self):
        print(11111)


xm = People("xm", 70, 1.7)
print(xm.bmi)

print(xm.name)
xm.name = "x_m"
print(xm.name)

del xm.name

