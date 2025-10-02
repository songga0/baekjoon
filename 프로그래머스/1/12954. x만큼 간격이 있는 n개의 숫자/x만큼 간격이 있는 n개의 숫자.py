def solution(x, n):
    answer = []
    i=0
    y=x
    for i in range(n):
        answer.append(y)
        y+=x
    return answer