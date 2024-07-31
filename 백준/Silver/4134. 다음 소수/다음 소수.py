import sys
from math import gcd

t=int(sys.stdin.readline())
for i in range(t):
    x=int(sys.stdin.readline())
    while(1):
        cnt=0
        if(x==0 or x==1):
            print(2)
            break
        else:
            for k in range(2,int(x**0.5)+1):
                if(x%k==0):
                    cnt+=1
                    break
            if(cnt==0):
                print(x)
                break
            else:
                x+=1