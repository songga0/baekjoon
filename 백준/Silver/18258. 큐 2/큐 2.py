import sys
from collections import deque
t=int(sys.stdin.readline())
lst=deque()
for i in range (t):
    x=sys.stdin.readline().split()
    if(x[0]=='push'):
        lst.append(x[1])
    elif(x[0]=='pop'):
        if lst:
            print(lst.popleft())
        else:
            print('-1')
    elif(x[0]=='size'):
        print(len(lst))
    elif(x[0]=='empty'):
        if lst:
            print('0')
        else:
            print('1')
    elif(x[0]=='front'):
        if lst:
            print(lst[0])
        else:
            print('-1')
    elif(x[0]=='back'):
        if lst:
            print(lst[-1])
        else:
            print('-1')