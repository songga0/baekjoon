import sys

k=int(sys.stdin.readline())

lst=[]

for i in range (k):
    n=int(sys.stdin.readline())
    if(n==0):
        lst.pop()
    else:
        lst.append(n)
print(sum(lst))