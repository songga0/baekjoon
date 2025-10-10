def solution(operations):
    answer = []
    for i in operations:
        x,y=i.split(' ')
        if x=='I':
            answer.append(int(y))
        else:
            if y=='1' and len(answer)>0:
                m=max(answer)
                answer.remove(m)
            elif y=='-1' and len(answer)>0:
                n=min(answer)
                answer.remove(n)
    if len(answer)==0:
        return [0,0]
    else:
        return [max(answer),min(answer)]