def solution(s):
    result=[]
    l=len(s)
    s=s*2
    final=0
    for i in range(l):
        result.append(s[i:i+l])
    for i in result:
        answer = []
        check=True
        for j in i:
            if j=='(' or j=='[' or j=='{':
                answer.append(j)
            elif j==')':
                if len(answer)>0 and '(' ==answer[-1]:
                    answer.pop()
                else:
                    check=False
                    break
            elif j=='}':
                if len(answer)>0 and '{' ==answer[-1]:
                    answer.pop()
                else:
                    check=False
                    break
            elif j==']':
                if len(answer)>0 and '[' ==answer[-1]:
                    answer.pop()
                else:
                    check=False
                    break
        if check==True and len(answer)==0:
            final+=1
    return final