import sys
from collections import deque

n=int(sys.stdin.readline())
result=deque()
for i in range(n):
    x=sys.stdin.readline().split()
    if(x[0]=='1'):
        result.appendleft(x[1])
    elif(x[0]=='2'):
        result.append(x[1])
    elif(x[0]=='3'):
        if result:
            print(result.popleft())
        else:
            print('-1')
    elif(x[0]=='4'):
        if result:
            print(result.pop())
        else:
            print('-1')
    elif(x[0]=='5'):
        print(len(result))
    elif(x[0]=='6'):
        if result:
            print('0')
        else:
            print('1')
    elif(x[0]=='7'):
        if result:
            print(result[0])
        else:
            print('-1')
    elif(x[0]=='8'):
        if result:
            print(result[-1])
        else:
            print(-1)