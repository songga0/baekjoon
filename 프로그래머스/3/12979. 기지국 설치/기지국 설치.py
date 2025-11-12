import math
def solution(n, stations, w):
    answer = 0
    answer=math.ceil((stations[0]-w-1)/(2*w+1))
    x=stations[0]+w
    for i in range(1,len(stations)):
        answer+=math.ceil((stations[i]-x-w-1)/(2*w+1))
        x=stations[i]+w
    answer+=math.ceil((n-x)/(2*w+1))
    return answer