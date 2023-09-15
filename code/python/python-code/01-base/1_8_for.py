# -*- coding: utf-8 -*-
"""
理解for循环的本质
1. 调用iter()，将numbers转化为迭代器numbers_iterator
2. 调用next(numbers_iterator)，返回出numbers的第一个元素
3. 循环步骤2,迭代完numbers内所有数据,捕获异常
"""

# while + iterator
numbers = [1, 2, 3, 4]
numbers_iterator = iter(numbers)
while True:
    try:
        print(next(numbers_iterator))
    except StopIteration:  # 捕捉异常终止循环
        break

# for循环
for i in numbers:
    print(i)
