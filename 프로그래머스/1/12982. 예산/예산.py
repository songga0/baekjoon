def solution(d, budget):
    newL=sorted(d)
    answer = 0
    check=True
    for i in newL:
        budget-=i
        answer+=1
        if(budget<0):
            check=False
            break
    if check==False:
        answer-=1
    return answer