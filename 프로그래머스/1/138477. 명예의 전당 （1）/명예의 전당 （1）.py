def solution(k, score):
    answer = []
    lst=[]
    for i in range(len(score)):
        lst.append(score[i])
        lst=sorted(lst)
        if len(lst)>k:
            lst=lst[1:]
        answer.append(lst[0])
    return answer