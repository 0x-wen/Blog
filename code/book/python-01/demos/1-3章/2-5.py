from collections import OrderedDict


order_dict = OrderedDict(name="xm", age=18)

print(order_dict)

for k, v in order_dict.items():
    print(k, v)

for i in range(5):
    order_dict[i] = i * 10

print(order_dict)

order_dict.move_to_end("age", last=False)
print(order_dict)



