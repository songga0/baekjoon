import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

dictionary = {}
for i in range(n):
    dictionary[num[i]] = -1

for i in range(len(check)):
    if(check[i] in dictionary):
        print('1',end=' ')
    else:
        print('0',end=' ')