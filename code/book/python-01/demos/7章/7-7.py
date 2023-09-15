from threading import Thread, Lock
import time

n = 100


def func():
    global n
    time.sleep(2)
    n = 666
    print("子线程:", n)


t = Thread(target=func)
t.start()
t.join()
print("主线程:", n)
