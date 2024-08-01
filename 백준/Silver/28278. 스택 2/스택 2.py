import sys

lst=[]
n=int(sys.stdin.readline())
for _ in range(n):
    x_list=sys.stdin.readline().split()
    x=x_list[0]
    if(x=='1'):
        lst.append(x_list[1])
    elif(x=='2'):
        if(lst):
            print(lst.pop())
        else:
            print(-1)
    elif(x=='3'):
        print(len(lst))
    elif(x=='4'):
        if(lst):
            print(0)
        else:
            print(1)
    elif(x=='5'):
        if(lst):
            print(lst[-1])
        else:
            print(-1)