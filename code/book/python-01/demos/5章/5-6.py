class Person:
    age = 10

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print("当访问不存在的属性时触发执行：__getattr__", item)
        return None

    def __setattr__(self, key, value):
        print("属性赋值时触发执行，__setattr__", key, value)
        # self.key = value
        # self.__dict__[key] = value
        if key == "name" and not isinstance(value, str):
            raise
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("当使用del回收对象属性时触发执行，__delattr__", item)
        if item == "age":
            raise
        self.__dict__.pop(item)



p = Person("xm")
print(p.name)
print(p.age)
print(p.__dict__)
p.age = 100
print(p.name)
p.name = "123"

del p.name
print("age", p.age)