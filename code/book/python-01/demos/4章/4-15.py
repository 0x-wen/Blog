class Ftp:
    def get(self):
        print("get...")

    def set(self):
        print("get...")

    def delete(self):
        print("delete...")


ftp = Ftp()
cmd = input('请输入指令：').strip()
print(getattr(ftp, cmd, 123))




# import sys
#
#
# def s1():
#     print('s1')
#
#
# def s2():
#     print('s2')
#
#
# this_module = sys.modules[__name__]
# print(hasattr(this_module, 's1'))
# getattr(this_module, 's2')
