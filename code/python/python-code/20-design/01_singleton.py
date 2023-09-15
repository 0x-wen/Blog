# -*- coding: utf-8 -*-
import threading
import time


# 使用__new__实现单例模式
class A:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj


a, b = A(), A()
print(id(a), id(b))


# 使用类方法实现单例模式
class B:
    __instance = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def singleton(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


# 使用装饰器实现单例
def singleton(cls):
    obj = {}

    def wrapper(*args, **kwargs):
        if not obj:
            obj[cls] = cls(*args, **kwargs)
        return obj[cls]

    return wrapper


@singleton
class C:
    pass


# 创造线程安全的单例模式
class D:
    __instance = None
    __lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def singleton(cls, *args, **kwargs):
        # 代码块中的代码自动加锁，被锁住的代码同一时间只有一个线程在执行
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls(*args, **kwargs)
        return cls.__instance


def create_obj():
    obj = B.singleton()
    print(id(obj))
    return obj


if __name__ == '__main__':
    # 1.创建10个线程
    tasks = [threading.Thread(target=create_obj) for _ in range(10)]
    # 2.同时启动线程
    for t in tasks:
        t.start()
