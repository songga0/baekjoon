def solution(arr1, arr2):
    x=len(arr1)
    y=len(arr2[0])
    answer=[[0 for _ in range(y)] for _ in range(x)]
    for i in range(x): 
        for k in range(len(arr2[0])):
            num=0
            for j in range(len(arr1[0])):
                num+=arr1[i][j]*arr2[j][k]
            answer[i][k]=num
    return answer