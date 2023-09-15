class MyType(type):

    def __call__(self, *args, **kwargs):
        print("我执行了")
        super().__call__(*args, **kwargs)


class People(object, metaclass=MyType):
    pass


p = People()