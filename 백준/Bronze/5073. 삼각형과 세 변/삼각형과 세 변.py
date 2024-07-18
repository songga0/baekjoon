while(1):
    a,b,c=map(int,input().split())
    len=[a,b,c]
    if(a==0 and b==0 and c==0):
        break
    else:
        if(max(len)>=(sum(len)-max(len))):
            print('Invalid')
        else:
            if(a==b==c):
                print('Equilateral')
            elif(a==b or b==c or c==a):
                print('Isosceles')
            else:
                print('Scalene')