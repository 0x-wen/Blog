# -*- coding: utf-8 -*-

# 在ipython中执行
a = 100
b = 100
print(a is b)		# True

a = 500
b = 500
print(id(a) == id(b))		# False

a, b = 500, 500
print(a is b)		# True		在同一行定义两个相同值的变量，此时解释器做了优化，执行一个内存地址

a = "abc"
b = "abc"
print(a is b)		# True

a = "abc!"
b = "abc!"
print(a is b)		# False

