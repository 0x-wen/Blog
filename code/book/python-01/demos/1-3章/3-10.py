names = ["张三", "李四", "王二", "麻子"]

# for i in range(len(names)):
#     print(i, names[i])

for i, name in enumerate(names, start=100):
    print(i, name)


names = {"a": 22, "b": 33, "c": 44}
for i, name in enumerate(names.items()):
    print(i, name)
