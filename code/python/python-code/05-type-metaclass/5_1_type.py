# -*- coding: utf-8 -*-

# 类也是对象,类的类型是 type, type是python默认元类。
def __init__(self, name):
    self.name = name


def say(self):
    return f"{self.name},会唱歌..."


# 使用type创建类的方式  本质上所有类都是type创建
Student = type("Student", (object,), {
    "__init__": __init__,
    "say": say,
})

if __name__ == '__main__':
    xiao_ming = Student("小明")
    print(Student)  # <class '__main__.Student'>
    print(xiao_ming.name)  # xiao_ming 是Student类创建的对象，name是对象的属性信息
    print(xiao_ming.say())
