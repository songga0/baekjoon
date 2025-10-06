def solution(n,a,b):
    #게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B
    answer = 0
    while(a!=b):
        answer+=1
        a=(a+1)//2
        b=(b+1)//2
    return answer

