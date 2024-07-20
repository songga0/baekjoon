import sys
input=sys.stdin.readline

s=str(input())

word=[]

for i in range(len(s)):
    for j in range(i+1,len(s)):
        word.append(s[i:j])
word=set(word)
print(len(word))
