# import abc
#
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Cat(Animal):
#     def talk(self):
#         print("猫说话")
#
#
# c = Cat()
# c.talk()


class Animal:
    def talk(self):
        raise NotImplementedError("该方法必须实现")

    def eat(self):
        pass


class Cat(Animal):
    def talk(self):
        print("猫说话")


c = Cat()
c.talk()