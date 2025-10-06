def solution(n, words):
    answer = 0
    LWord=words[0][0]
    check=True
    for i in range(len(words)):
        answer+=1
        if words[i].startswith(LWord)==False:
            check=False
            break
        elif words[i] in words[:i]:
            check=False
            break
        else:
            LWord=words[i][-1]
            
    if len(words)==answer and check==True:
        return [0,0]
    else:
        num=answer%n
        if num==0:
            num=n
        time=answer//n
        if answer%n>0:
            time+=1
        return num,time