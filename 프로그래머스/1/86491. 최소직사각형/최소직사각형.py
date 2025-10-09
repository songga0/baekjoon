def solution(sizes):
    answer = 0
    mn=[]
    mx=[]
    for i in sizes:
        if i[0]>i[1]:
            mx.append(i[0])
            mn.append(i[1])
        else:
            mx.append(i[1])
            mn.append(i[0])
    return max(mn)*max(mx)