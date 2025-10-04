def solution(n):
    answer = 0
    for start in range(1, n + 1):
        total = 0
        current = start
        while total < n:
            total += current
            current += 1
        if total == n:
            answer += 1
    return answer
