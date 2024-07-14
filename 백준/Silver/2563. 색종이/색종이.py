n=int(input())
a= [[0 for _ in range(100)] for _ in range(100)]
cnt=0

for i in range (100):
    for j in range(100):
        a[i][j]=0

for k in range (n):
    x,y=map(int,input().split())
    for i in range (x,x+10):
        for j in range (y,y+10):
            a[i][j]=1

for i in range (100):
    for j in range(100):
        if(a[i][j]==1):
            cnt+=1

print(cnt)