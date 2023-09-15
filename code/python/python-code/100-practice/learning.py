# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 16:05
# @Author  : Jw
# @File    : learning.py

#  统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

num1 = len([i for i in [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] if i > 0])
num2 = len([i for i in [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] if i < 0])
print(num1, num2)

# 字符串 “axbyczdj”，如果得到结果“abcd”
str1 = "axbyczdj"
str2 = str1[0::2]
print(str2)

# 冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6, 90, 2]
for i in range(len(a)):
    for j in range(0, len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

# 排序去重
a = [1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

aa = [1, 3, 6, 9, 7, 3, 4, 6]

b = list(set(aa))
b.sort(key=aa.index)
print(b)


# 递归问题

from functools import reduce

num = reduce(lambda x,y : x*y , range(1,5))
print(num)