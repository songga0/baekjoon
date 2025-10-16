def solution(A, B):
    answer = 0
    A=sorted(A)
    B=sorted(B)
    for i in A:
        for j in B:
            if i<j:
                answer+=1
                B.remove(j)
                break
    return answer