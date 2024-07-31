import sys
prime_list=[True for _ in range(1000001)]

for i in range(2,1000001):
    if prime_list[i]==True:
        for j in range(i*2,1000001,i):
            prime_list[j]=False
                

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    result=0
    for i in range(2,n//2+1):
        if(prime_list[i] and prime_list[n-i]):
            result+=1
    print(result)