n=int(input())
xlist=[]
ylist=[]

for i in range(n):
    x,y=map(int,input().split())
    xlist.append(x)
    ylist.append(y)

xmin=min(xlist)
xmax=max(xlist)
ymin=min(ylist)
ymax=max(ylist)

print((xmax-xmin)*(ymax-ymin))