import sys
n=int(sys.stdin.readline())

work={}

for i in range(n):
    name,enter=sys.stdin.readline().split()
    if (enter=='enter'):
        work[name]=True
    else:
       del  work[name]

work=sorted(work.keys(),reverse=True)

for i in work:
    print(i)