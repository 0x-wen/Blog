from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(11, y=22)

print(p[0], p[1])
print(p.x, p.y)
print(p._asdict())

d = {"x": 10, "y": 100}
print(Point(**d))

new_p = p._replace(y=100)
print(p)
print(new_p)
