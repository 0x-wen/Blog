# -*- coding: utf-8 -*-

"""推导式"""
"""1.列表推导式
普通使用： [ i for i in XXX]
结合条件一起使用： [ i for i in XXX if 条件]
"""
# 需求：如何快速生成一个["data0", "data1", ..."data99"]的列表？
result1 = ["data" + str(i) for i in range(0, 100)]
print(result1)
# 需求：如何快速生成一个["data0", "data2","data4", ..."data98"]的列表？
result2 = ["data{}".format(i) for i in range(0, 100) if i % 2 == 0]
print(result2)

"""2.字典推导式
dict1 = { key:value for i in XXX}
"""
# 需求：将一个字符串转换为字典格式的数据 name=zs;age=18
one_str = "name=zs;age=18"
one_list = one_str.split(';')  # ['name=zs', 'age=18']
dict1 = {i.split("=")[0]: i.split("=")[1] for i in one_list}
print(dict1)  # {'name': 'zs', 'age': '18'}

# 实现 {'data1':1, "data2":2, "data3":3}
print({f"data{(i + 1)}": i + 1 for i in range(3)})  # {'data1': 1, 'data2': 2, 'data3': 3}
print([i for i in range(4) if i % 2 == 0])
