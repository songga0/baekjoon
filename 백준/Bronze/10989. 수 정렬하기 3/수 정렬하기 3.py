import sys

n = int(input())
num = [0]*10001
for _ in range(n):
    num[int(sys.stdin.readline())]+=1

for i in range(len(num)):
    if(num[i]!=0):
        for j in range(num[i]):
            print(i)