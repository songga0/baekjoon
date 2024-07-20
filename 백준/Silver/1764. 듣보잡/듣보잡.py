import sys
input=sys.stdin.readline

n,m=map(int,input().split())

l=[]
for i in range (n):
    name=input()
    l.append(name)

s=[]
for i in range(m):
    name=input()
    s.append(name)

answer = list(set(l) & set(s))
answer.sort()
print(len(answer))
print(''.join(answer), end = '')