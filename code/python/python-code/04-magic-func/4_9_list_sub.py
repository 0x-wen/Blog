# -*- coding: utf-8 -*-

# 为list添加相减操作
class MyList(list):
    def __sub__(self: list, other: list):
        for i in other:
            if i in self:
                self.remove(i)
        return self


def main():
    one_list = MyList([1, 2, 3, 4, 5])  # self: list
    two_list = [3, 4, 6]  # other: list
    print(one_list - two_list)


if __name__ == '__main__':
    main()
