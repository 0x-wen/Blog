from threading import Thread


def task(a):
    print("我是子线程")


class MyThread(Thread):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def run(self):
        task(self.a)


t = MyThread("123")
t.start()
print("主线程")
