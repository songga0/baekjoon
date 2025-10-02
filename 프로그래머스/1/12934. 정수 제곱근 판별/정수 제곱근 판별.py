def solution(n):
    answer = -1
    num=int(n**0.5)
    if(n==num**2):
        answer=(num+1)**2
    return answer