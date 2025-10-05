def solution(brown, yellow):
    answer = []
    x=1
    y=1
    for i in range(1,brown):
        x=i
        check=False
        for j in range(1,brown):
            y=j
            if i*j==yellow and 2*(x+y)+4==brown:
                check=True
                break
        if check==True:
            break
    if x>y: 
        answer=[x+2,y+2]
    else:
        answer=[y+2,x+2]
    return answer