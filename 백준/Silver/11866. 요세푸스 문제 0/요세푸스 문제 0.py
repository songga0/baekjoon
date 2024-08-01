import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

q=list(range(1,n+1))
result=[]

i=0
while(len(q)>0):
    i=i+(k-1)
    if(i>=len(q)):
        while(i>=len(q)):
            i=i-len(q)
    temp=q[i]
    q.remove(temp)
    result.append(temp)

print('<',end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(result[-1],end='')
print('>')
