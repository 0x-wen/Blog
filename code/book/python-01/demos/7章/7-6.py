from threading import Thread


def task():
    print("我是子线程")


t = Thread(target=task)
t.start()
print("我是主线程")
