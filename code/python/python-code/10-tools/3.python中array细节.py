# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 14:53
# @Author  : Jw
# @File    : 3.python中array细节.py

from array import array

# 这是python内置库中的数组

a = array('b', [1, 2, 3, 2, 2, 2, 2, 5])
print(a.count(2))  # 返回一个值出现的次数
for i in a:
    print(f'{i}', end=',')  # 更改了输出方式
print()

# 使用切片获取
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = array('i', numbers_list)

print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])  # beginning to end

print("-------------------------")
# obj = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7]u
obj = ['\u6211', '\u7684', 'v']  # 要存中文信息，只能使用Unicode字符集
my_array = array('u', obj)

print(my_array)


# 小练习 撸一个数组
class MyArray:
    # 1.一个数组，要有长度，要有类型。所以__init__ 构造方法中要有index 和创建一个 存数据的list

    def __init__(self, index):
        self._data = []
        self._index = index

    # 2.数据怎么存？
    # list中的insert 可以存数据，这里要解决，1.存数据类型 2.长度判断
    def insert(self, index: int, value: int) -> object:
        if not isinstance(value, int):
            print('fail,check your data.')
            return False
        # 这里是判断 插入值的index 超过 数组长度   例： 数组为10 你要把数据放在下标为11的，怎么处理？
        if index >= self._index:
            print('insert out of range.')
            return False
        # 这里是判断 数组中已有元素的长度 和 数组限制长度对比
        if len(self) >= self._index:
            print('self out of range.')
            return False
        return self._data.insert(index, value)

    # 发现数组长度问题未得到解决，需要使用 对象的长度 和 构造方法中的 index作对比，只有小于时才能像数组中添加元素
    def __len__(self):
        return len(self._data)

    # 3.解决删 查
    def remove(self, index: int):
        return self._data.pop(index)

    def find(self, index: int):
        return self._data[index]

    # 4.还要解决将array数据全部输出的问题
    # 1/将数据变成一个生成器
    def __iter__(self):
        for item in self._data:
            yield item

    # 2/将生成器遍历之后输出值
    def print_array(self):
        for item in self:
            print(item)


def test_main():
    print('******************my_array********************')
    obj1 = MyArray(index=5)
    obj1.insert(index=0, value=9)
    obj1.insert(index=1, value=8)
    obj1.insert(index=0, value=7)
    obj1.insert(index=0, value=6)
    obj1.insert(index=4, value=5)
    assert obj1.insert(index=5, value=4) is False
    obj1.print_array()  # [6,7,9,8,5]
    print(obj1.find(index=4))  # 5
    print('数组中 通过下标查询的时间复杂度为O(1)')
    print('删除和插入数据 时间复杂度为O(n),数组在内存中存储,需要一块连续的内存空间,因为删除和插入数据 其他数据都需要偏移')


def test_python_array():
    python_array = array('i', [1])
    print(python_array)
    python_array.insert(0, 3)
    python_array.insert(1, 4)
    python_array.insert(2, 4)
    print(python_array)


if __name__ == '__main__':
    test_main()
