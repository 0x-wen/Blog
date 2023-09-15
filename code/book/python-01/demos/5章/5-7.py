
class Person(object):

    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print("使用[]获取属性时触发，__getitem__", item)
        return self.__dict__.get(item, "不存在")

    def __setitem__(self, key, value):
        print("使用[]给对象赋值时触发 __setitem__", key, value)
        self.__dict__[key] = value
        # setattr(self, key, value)

    def __delitem__(self, key):
        print("使用[]做属性回收del时触发执行__delitem__", key)
        # del p.name
        self.__dict__.pop(key)


p = Person("xm")
print(p.name)
print(p["age"])

p["name"] = "x_M"
print(p.name)

del p["name"]
print(p.name)