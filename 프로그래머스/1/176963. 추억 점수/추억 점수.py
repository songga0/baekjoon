def solution(name, yearning, photo):
    answer = []
    for i in photo:
        x=0
        for j in i:
            if j in name:
                x+=yearning[name.index(j)]
            else:
                continue
        answer.append(x)
    return answer