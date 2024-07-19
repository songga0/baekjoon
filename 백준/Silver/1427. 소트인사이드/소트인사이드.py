import sys

num=[]
num=list(map(str,input()))
num=[row for row in num]
for i in range (len(num)):
    num[i]=int(num[i])

for i in sorted(num,reverse=True):
    print(i,end='')