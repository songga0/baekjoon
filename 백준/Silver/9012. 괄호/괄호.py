import sys

t=int(sys.stdin.readline())

for i in range (t):
    result=[]
    x=0
    lst=[]
    lst.extend(list(sys.stdin.readline().strip()))
    for i in lst:
        if (i=='('):
            result.append(i)
        elif(i==')'):
            if (result):
                result.pop()
            else:
                x=1
                break
    if (result):
        x=1
    if(x==1):
        print('NO')
    else:
        print('YES')