import sys

n_list = list(range(2,246913))
prime_list=[]
for i in n_list:
    cnt=0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            cnt+=1
            break
    if(cnt==0):
            prime_list.append(i)


while(1):
    n=int(sys.stdin.readline())
    if(n==0):
        break
    else:
        if(n==1):
            print(1)
        else:
            count=0
            for i in prime_list:
                if n<i<=n*2:
                    count+=1
            print(count)
