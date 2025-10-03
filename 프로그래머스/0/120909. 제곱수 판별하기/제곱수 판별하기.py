def solution(n):
    answer = 2
    num=int(n**0.5)
    if n==num**2:
        answer=1
    return answer