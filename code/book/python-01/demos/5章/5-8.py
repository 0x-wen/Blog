# file = open("text.txt", "w")
# file.write("hello world")
# file.close()

# with open("text.txt", "w") as f:
#     f.write("hello world")
#
# print("ok")


class MyOpen:
    def __init__(self, file_name, mode):
        self.file = open(file_name, mode)

    def __enter__(self):
        print("进入with局域块时触发 __enter__")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出with局域块时触发 __exit__")
        self.file.close()
        print(exc_type, exc_val, exc_tb)



with MyOpen("text.txt", "w") as f:
    f.write("hello world")
    raise ValueError("ok")

print("1111")