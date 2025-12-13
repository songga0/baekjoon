def solution(a, b):
    answer = ''
    days=b
    a-=1
    while(a>0):
        if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
            days+=31
        elif a==4 or a==6 or a==9 or a==11:
            days+=30
        else:
            days+=29
        a-=1
    if days%7==0:
        return "THU"
    elif days%7==1:
        return "FRI"
    elif days%7==2:
        return "SAT"
    elif days%7==3:
        return "SUN"
    elif days%7==4:
        return "MON"
    elif days%7==5:
        return "TUE"
    else:
        return "WED"