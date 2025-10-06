def solution(n):
    answer = 1
    num1=1
    num2=2
    if n==2:
        answer=2
    elif n>=3:
        for i in range(3,n+1):
            answer=num1+num2
            num1=num2
            num2=answer
    return answer%1234567