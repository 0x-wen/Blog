x = 10

def outer():

    def inner():
        return x + 1

    return inner


f = outer()

print(f.__closure__)
