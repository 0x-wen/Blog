# # 普通写法：
# nums = []
# for i in range(1, 101):
#     nums.append(i*i)
#
# # 推导式写法：
# nums = [i*i for i in range(1, 101)]
# print(nums)
# nn = [1,2,3,4,5,6,7,8,9,10]
# nums = [i for i in nn if i % 2 == 0 if i in [2, 6]]
# print(nums)

# a = {"name": "xm", "age": 18}
# keys = [k for k in a.keys()]
# print(keys)

# ll = [1,2,3,4,5]        # ["1", "2", ...]
# ll = [str(i) for i in ll]

# nums = {i: i * 2 for i in range(5)}
# print(nums)

# nums = {i for i in range(10)}
# print(nums)

# nums = tuple(i for i in range(10))
# print(nums)

# a = (10,)
a = 10,

print(type(a))

