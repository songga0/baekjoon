import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

dict = {}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for i in check:
    if i in dict:
        print(dict[i],end=' ')
    else:
        print('0',end=' ')