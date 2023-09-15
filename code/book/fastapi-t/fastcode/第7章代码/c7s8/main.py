class MyFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("进入with...")
        return self		# 返回的数据赋值给p

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with")


with MyFile('jack') as p:
    print(p.name)
