def solution(routes):
    routes.sort(key=lambda x: x[1])
    cam=[]
    cam.append(routes[0][1])
    answer = 1
    for i in routes:
        check=False
        for j in cam:
            if i[0]<=j and j<=i[1]:
                check=True
        if check==False:
            answer+=1
            cam.append(i[1])
    return answer