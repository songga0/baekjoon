def solution(s):
    answer = []
    zero=0
    cnt=0
    while(True):
        zero+=s.count('0')
        one=s.count('1')
        s = bin(one)[2:] 
        cnt+=1
        if s=='1':
            break
    return [cnt,zero]