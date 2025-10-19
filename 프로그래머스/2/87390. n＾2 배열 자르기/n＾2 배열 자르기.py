def solution(n, left, right):
    res = []
    for idx in range(left, right+1):
        i = idx // n   # 행
        j = idx % n    # 열
        res.append(max(i, j) + 1)
    return res
