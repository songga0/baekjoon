import sys
a1, a2 = map(int,sys.stdin.readline().split())
b1, b2 = map(int,sys.stdin.readline().split())

y=a2*b2
x=a1*b2+a2*b1


aa, bb = x, y
while bb != 0:   
    aa,bb=bb,aa%bb

print(x//aa,y//aa)