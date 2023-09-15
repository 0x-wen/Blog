import time


def outer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return inner


@outer
def foo():      # foo = outer(foo)
    time.sleep(2)



# foo = outer(foo)


foo()


