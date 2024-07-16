n,k=map(int,input().split())
cnt=1
i=1
num=[]
for i in range (1,n+1):
    if(n%i==0):#약수인 경우
        num.append(i) #num에 약수추가
        cnt+=1 #몇번째 약수인지 저장
        i+=1
    else:
        i+=1

if(len(num)<k):
    print('0')
else:
    print(num[k-1])