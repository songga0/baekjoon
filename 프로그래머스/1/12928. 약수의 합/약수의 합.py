def solution(n):
    answer = 0
    i=1
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            if(i**2==n):
                answer+=i
            else:
                answer=answer+i+(n//i)
    return answer