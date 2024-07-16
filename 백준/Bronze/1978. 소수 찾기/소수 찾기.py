n=int(input())
num=input().split()
result=0

for i in range(n):
    x=int(num[i])+1
    cnt=0
    for j in range(1,x):
        if(int(num[i])%j==0):
            cnt+=1
    if(cnt==2):
        result+=1

print(result)
        