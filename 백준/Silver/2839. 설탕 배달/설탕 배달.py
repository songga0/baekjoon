n=int(input())
num=n
i=num//5

while(1):
    if(i>=0):
        num=n
        num=num-(i*5)
        if(num%3==0):
            print(i+num//3)
            break
        else:
            i=i-1
    else:
        print('-1')
        break