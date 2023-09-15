# list1 = [1, 2, [11, 22]]
# list2 = list1				# 变量赋值操作
#
# print(id(list1))
# print(id(list2))

list1 = [1, 2, [11, 22]]
list2 = list1.copy()
print(id(list1[2]))
print(id(list2[2]))

list1[0] = 100
list1[2][0] = 111

print(list1)
print(list2)

from copy import deepcopy
list1 = [1, 2, [11, 22]]
list2 = deepcopy(list1)
print(id(list1[2]))
print(id(list2[2]))

list1[0] = 100
list1[2][0] = 111

print(list1)
print(list2)
