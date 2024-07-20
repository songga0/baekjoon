import sys
n,m=map(int,sys.stdin.readline().split())

s=[]
for i in range(n):
    s.append(sys.stdin.readline())

check=[]
for i in range(m):
    check.append(sys.stdin.readline())

cnt=0
for i in check:
    if (i in s):
        cnt+=1
print(cnt)