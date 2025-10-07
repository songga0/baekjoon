def solution(s):
    up=''
    down=''
    for i in s:
        if i.isupper():
            up+=i
        else:
            down+=i
    answer = ''.join(sorted(down,reverse=True))+''.join(sorted(up,reverse=True))
    return answer