while(1):
    n=int(input())
    if(n!=-1):
        num=[]
        sum=0

        for i in range (1,n):
            if(n%i==0):
                num.append(i)

        for i in range(len(num)):
            sum=sum+num[i]

        if(sum==n):
            print(n,'=',end=' ')
            for i in range(len(num)-1):
                print(num[i],end=' + ')
            print(num[len(num)-1])
        else:
            print(n,'is NOT perfect.')
    else:
        break