import sys
from math import gcd

n=int(sys.stdin.readline())
a=[]
a1=int(sys.stdin.readline())
for i in range(n-1):
   num=int(sys.stdin.readline())
   a.append(num-a1)
   a1=num

g=a[0]
for i in range(1,len(a)):
   g=gcd(g,a[i])

result=0
for i in a:
   result+=i//g-1

print(result)
   