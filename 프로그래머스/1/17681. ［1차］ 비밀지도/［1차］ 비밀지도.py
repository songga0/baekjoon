def solution(n, arr1, arr2):
    answer = []
    x=[]
    for i in range(len(arr1)):
        x.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
    for i in x:
        y=''
        for j in i:
            if j=='1':
                y+='#'
            else:
                y+=' '
        answer.append(y)
    return answer