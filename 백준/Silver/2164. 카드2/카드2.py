import sys
from collections import deque
n=int(sys.stdin.readline())
lst=deque(range(1,n+1))

while(len(lst)>1):
    temp=lst.popleft()
    temp=lst.popleft()
    lst.append(temp)

print(lst[0])