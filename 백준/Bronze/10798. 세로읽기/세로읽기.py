row=[]
length = []
ans = ''
for _ in range(5):
    line=input()
    length.append(len(line))
    row.append(line)



for j in range(max(length)):
    for i in range(5):
        if j< length[i]:
            ans+=row[i][j]

print(ans)