import sys
n=int(input())
num=[]
for i in range (n):
    x,y=map(int,input().split())
    num.append([x,y])

num.sort()
for i in num:
    print(i[0],i[1])