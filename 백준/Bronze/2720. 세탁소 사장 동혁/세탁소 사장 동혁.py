t=int(input())

for i in range (t):
    c=int(input())
    result=c//25
    print(int(result), end=' ')
    c=c%25
    result=c//10
    print(int(result),end=' ')
    c=c%10
    result=c//5
    print(int(result),end=' ')
    c=c%5
    print(int(c))
    