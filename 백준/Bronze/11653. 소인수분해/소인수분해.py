n=int(input())
num=0
i=2

while(n>1):
    #소수인것 찾기
    if(n%i==0):
        print(i)
        n=n/i
    else:
        i+=1
       