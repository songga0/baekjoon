n=int(input())
x=2
if (n==0):
    print('4')
else:
    for i in range(n):
        x=x+(x-1)
    print(x*x)