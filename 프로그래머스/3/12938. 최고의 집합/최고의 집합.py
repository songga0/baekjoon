def solution(n, s):
    answer = []
    if s//n<=0:
        return [-1]
    else:
        x=s//n
        for _ in range(n):
            answer.append(x)
        for i in range(s % n):
            answer[i] += 1
    return sorted(answer)