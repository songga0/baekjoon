a,b=map(int,input().split())

x=0
y=0

x=a//100
a=a%100
y=a//10
a=a%10
a=a*100+y*10+x

x=b//100
b=b%100
y=b//10
b=b%10
b=b*100+y*10+x

if(a>b):
    print(a)
else:
    print(b)