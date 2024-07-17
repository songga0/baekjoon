a,b,c=map(int,input().split())
l=[a,b,c]
sum=a+b+c-max(l)
if(sum>max(l)):
    print(a+b+c)
else:
    print(sum*2-1)