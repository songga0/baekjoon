n=int(input())
cnt=1
i=1
if (n==1):
    print(cnt)
else:
    n=n-1
    while(n>0):
        n=n-(6*i)
        i+=1
        cnt+=1
    print(cnt)
