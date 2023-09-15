# from collections import defaultdict
#
# dd = defaultdict(int)
#
# print(dd)
#
# # dd[1] = 10
# dd[1] += 1      # dd[1] = dd[1] + 1
# print(dd)


# from collections import defaultdict
#
# dd = defaultdict(list)
#
# dd["a"].append(1000)
# print(dd["a"])


from collections import defaultdict


def default_value():
    return list()


dd = defaultdict(default_value)

print(dd["num"])





