x=[]
max=0
maxi,maxj=0,0
for i in range (9):
    row=list(map(int,input().split()))
    x.append(row)
    for j in range (9):
        if(x[i][j]>=max):
            max=x[i][j]
            maxi=i+1
            maxj=j+1

print(max)
print(maxi, maxj)