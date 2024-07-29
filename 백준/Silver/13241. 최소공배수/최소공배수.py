a, b = map(int,input().split())
aa, bb = a, b
while bb != 0:   
    temp = aa
    aa = bb     
    bb = temp % bb  
print(a * b // aa)   