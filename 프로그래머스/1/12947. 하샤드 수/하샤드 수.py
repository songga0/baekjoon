def solution(x):
    answer = False
    num=0
    y=x
    while(y>0):
        num+=y%10
        y=y//10
    if(x%num==0):
        answer=True
    return answer