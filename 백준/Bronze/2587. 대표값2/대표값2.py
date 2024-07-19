num=[]
for i in range (5):
    x=int(input())
    num.append(x)

print(sum(num)//len(num))

num.sort()
print(num[len(num)//2])