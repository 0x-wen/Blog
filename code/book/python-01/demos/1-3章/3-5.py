import time


def wrapper(flag):
    def outer(func):
        def inner(*args, **kwargs):
            start = time.time()
            rets = func(*args, **kwargs)
            print(rets)
            end = time.time()
            if flag == "am":
                print(f"{func}运行用时(am): {end - start} s")
            elif flag == "pm":
                print(f"{func}运行用时(pm): {end - start} s")
            print(end - start)

        return inner
    return outer


@wrapper("pm")
def foo(x, y):
    time.sleep(2)
    return x + y


foo(1, 3)       # inner(1, 3)
