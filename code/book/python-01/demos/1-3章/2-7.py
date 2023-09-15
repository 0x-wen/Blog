from collections import deque

dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)
dq.appendleft(100)
dq.appendleft(200)

print(dq)

print(dq.pop())
print(dq)
print(dq.popleft())

print(dq)

ll = [1, 2, 3, 4, 5]
dq = deque(ll)
print(dq.)
