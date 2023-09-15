import time

class MyRange:
    def __init__(self, total, step):
        self.count = -1
        self.total = total
        self.step = step

    def __iter__(self):
        print("11111")
        return self

    def __next__(self):
        self.count += self.step
        time.sleep(0.5)
        if self.count >= self.total:
            raise StopIteration
        return self.count


for i in MyRange(10, 1):
    print(i)
