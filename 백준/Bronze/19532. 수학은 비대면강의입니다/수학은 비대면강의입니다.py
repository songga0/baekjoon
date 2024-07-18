num=list(map(int,input().split()))

for i in range(-999,1000):
    for j in range(-999,1000):
        if(i*num[0]+j*num[1]==num[2] and i*num[3]+j*num[4]==num[5]):
            print(i,j)
            break