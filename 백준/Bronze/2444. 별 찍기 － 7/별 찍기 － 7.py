n=int(input())

for i in range (1,n):
    print(' '*(n-i),end='')
    print('*'*(2*i-1))
for i in range (n):
    print(' '*i,end='')
    print('*'*((n-i)*2-1))
