import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
result = []

while q:
    index, value = q.popleft()
    result.append(index)
    
    if not q:
        break
    
    if value > 0:
        q.rotate(-(value - 1))
    else:
        q.rotate(-value)

print(" ".join(map(str, result)))
