def solution(clothes):
    answer = 1
    cloth={}
    for i in clothes:
        if i[1] not in cloth:
            cloth[i[1]]=1
        else:
            cloth[i[1]]+=1
    for i in cloth.values():
        answer*= i+1
    return answer-1