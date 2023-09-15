# -*- coding: utf-8 -*-

# b引用a所指向的数据
a = 100
b = a
assert id(a) == id(b)
assert a is b

a = 100
b = a
a = 200
print(a, b)  # 200 100
assert a is not b
assert id(a) != id(b)

a1 = "str"
b1 = a1
a1 = "string"
print(a1, b1)  # string str

a = [1, 2, 3, 4]
b = a
a[0] = 100
print(a[0], b[0])  # 100, 100
assert a is b
assert id(a) == id(b)
