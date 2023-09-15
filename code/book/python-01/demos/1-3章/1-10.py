from itertools import chain
#
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# c = {"k1": "v1", "k2": "v2"}
#
#
# for i in chain(a, c.items()):
#     print(i)

b = [[1, 2], [3, 4], [5, 6]]        # [1,2,3,4,5,6]

# *b  ->  [1, 2], [3, 4], [5, 6]
# tmp = []
# for i in b:
#     for j in i:
#         tmp.append(j)

# for i in chain(*b):
#     print(i)


ll = set(chain(*b))
print(ll)



