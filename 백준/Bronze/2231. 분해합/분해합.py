n=int(input())

for i in range(1,n+1):
    num=list(map(int,str(i)))
    s=sum(num)+i
    if(s==n):
        print(i)
        break
    if(i==n):
        print(0)