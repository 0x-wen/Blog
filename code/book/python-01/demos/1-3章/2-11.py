# l1 = [5,2,8,1,4,5]
# l2 = [6,1,9,3,8,2]
#
# l1.sort(reverse=True)
# print(l1)
# print(sorted(l2, reverse=True))
#
#
# l1.sort(key=)

ll = [{"id": 5}, {"id": 1}, {"id": 3}]

# def sort(x):
#     return x["id"]
#
# ll.sort(key=sort)
weights = {3: 199, 5: 200, 1: 1000}
ll.sort(key=lambda x: weights[x["id"]])
print(ll)



