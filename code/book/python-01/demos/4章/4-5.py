from functools import cached_property


class Student:
    @cached_property
    def add(self):
        # 高计算资源消耗的实例特征属性
        print(111)
        fi = []
        a, b = 1, 1
        fi.append(a)
        for i in range(50 - 1):
            a, b = b, a + b
            fi.append(a)
        return fi


stu = Student()
print(stu.add)
print(stu.add)
print(stu.add)
print(stu.add)



