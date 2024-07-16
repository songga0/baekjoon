xlist=[]
ylist=[]
xresult=0
yresult=0

for i in range (3):
    x,y=map(int,input().split())
    xlist.append(x)
    ylist.append(y)
#xlist=[5, 5, 7]
#ylist=[5, 7, 5]
for i in range(3):
    cnt=0
    cnt=xlist.count(xlist[i])
    if(cnt==1):
        xresult=xlist[i]
    cnt=0
    cnt=ylist.count(ylist[i])
    if(cnt==1):
        yresult=ylist[i]

print(xresult,yresult)