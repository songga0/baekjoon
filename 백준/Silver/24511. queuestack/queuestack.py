import sys
from collections import deque

n = int(sys.stdin.readline())
queue=deque()

a=sys.stdin.readline().split()
b=sys.stdin.readline().split()
m=int(sys.stdin.readline())
c=sys.stdin.readline().split()
for i in range(n):
    if(a[i]=='0'):
        queue.appendleft(b[i])

for i in range(m):
    queue.append(c[i])
    print(queue.popleft(),end=' ')