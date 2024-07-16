m=int(input())
n=int(input())
num=[]
sum=0
#m이상 n이하 소수인것 찾기
for i in range(m,n+1):
    cnt=0
    for j in range (1,i+1):
        if(i%j==0):
            cnt+=1
    if(cnt==2):
        num.append(i)

if(len(num)==0):
    print('-1')
else:
    #소수합 출력
    for i in range(len(num)):
        sum=sum+num[i]

    print(sum)
    #가장 작은 소수 출력
    print(num[0])