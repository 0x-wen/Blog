def f1():
    yield 1
    yield from f2()
    yield 2


def f2():
    yield 3
    yield 4


generator = f1()		# f1()是生成器

for i in generator:
    print(i)			# 依次打印：1 3 4 2
