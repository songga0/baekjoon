def solution(triangle):
    l = len(triangle)
    for i in range(l-2,-1,-1):
        ln=len(triangle[i])
        for j in range(ln):
            m=max(triangle[i+1][j],triangle[i+1][j+1])
            triangle[i][j]+=m
    return triangle[0][0]