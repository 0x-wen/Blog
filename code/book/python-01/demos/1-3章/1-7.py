import sys

x = 10
print(sys.getrefcount(x))
y = x
print(sys.getrefcount(x))
z = 10
print(sys.getrefcount(x))
del z
print(sys.getrefcount(x))

