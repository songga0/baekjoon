import sys

m,n=map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    cnt=0
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            cnt+=1
            break
    if(cnt==0):
        print(i)
