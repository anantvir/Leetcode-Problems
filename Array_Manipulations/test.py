from collections import deque

deq = deque()

deq.append(2)
deq.append(3)
deq.append(1)
deq.append(6)

print(deq)
deq.pop()
print(deq)
deq.appendleft(99)
print(deq)