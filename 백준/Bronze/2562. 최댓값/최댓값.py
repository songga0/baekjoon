num=[]
for i in range (9):
    num.append(int(input()))
n=0
max=num[0]
for i in range (9):
    if num[i]>max:
        max=num[i]
        n=i

print(max)
print(n+1)