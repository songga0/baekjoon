def solution(num_list):
    answer = 0
    x=1
    for i in num_list:
        x*=i
    y=sum(num_list)**2
    if x<y:
        answer=1
    return answer