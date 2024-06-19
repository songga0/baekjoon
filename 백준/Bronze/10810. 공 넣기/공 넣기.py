n,m=map(int,input().split())
b=[0]*n
for x in range(m):
    i,j,k=map(int,input().split())
    for y in range(i,j+1):
        b[y-1]=k
        
for x in range(n):
    print(b[x],end=" ")