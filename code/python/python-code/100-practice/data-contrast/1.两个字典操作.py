# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 16:45
# @Author  :  Jw
# @File    : 1.两个字典操作.py

def two_dict_compare(a_dict, b_dict):
    """两个字典对比,a比b多哪些keys"""
    return set(a_dict) - set(b_dict)


headers1 = {"website": "12", "age": 1996}
headers2 = {"Connection": "open", "Ws_Code": "fu", "htc-x-type": "6", "Content-Type": "application/json",
            "website": "12", "age": 1996}
headers3 = {"Connection": "close", "Ws-Code": "feelunique", "htc-x-type": "3", "Content-Type": "application/json",
            "age": 1996}

# 判断a比b多哪些keys
one = two_dict_compare(headers1, headers2)
print(one, type(one), bool(one))
print(two_dict_compare(headers2, headers1))

print("\n{:*^50s}".format("1.对比a 比 b 多哪些key"))
keys = set(headers2) - set(headers3)
print(f"headers2比headers3多哪些key：{keys}")
print(f"headers3比headers2多哪些key：{set(headers3) - set(headers2)}")
print(f"set无序集合 查看headers2的keys和value:{set(headers2.items())}")
print(f"查看headers2和headers3相同的键值对:{headers2.items() & headers3.items()}")

print("\n{:*^50s}".format("判断response_data是否包含check_data"))
check_data, response_data = set(headers1.items()), set(headers2.items())
print(check_data)
print(response_data)
print(check_data.issubset(response_data))

print("\n{:*^50s}".format("2.简单对比2个字典是否相等"))
a = {"name": "张三", "age": 13}
b = {"name": "张三", "age": 13}
print(f"a和b两个字典是否相等：({a == b}),True, a字典的内存地址是：{id(a)}, b字典的内存地址是：{id(b)},\n "
      f"两个字典内容相等,那么a就是b吗？不是。内存不一定,返回结果为:{a is b}")

print("\n{:*^50s}".format("3.a对比b多哪些key 和 value值是多少"))
a1 = {"name": "张三", "age": 13, "city": "shenzhen", "sex": "男"}
b1 = {"name": "张三", "age": 13}
values = {i: a1.get(i) for i in set(a1.keys()) - set(b1.keys())}  # 第一种写法
print(values)
print(values_2 := set(a1.items()) ^ set(b1.items()))  # 第二种写法

print("\n{:*^50s}".format("4.a和b比较,相等key,不同值,分别的值是多少？"))
