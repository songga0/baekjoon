def solution(t, p):
    answer = 0
    l=len(str(p))
    for i in range(len(t)-l+1):
        x=t[i:i+l]
        if x<=p:
            answer+=1
    return answer