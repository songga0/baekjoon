def solution(cacheSize, cities):
    answer = 0
    city=[]
    if cacheSize>0:
        for i in range(len(cities)):
            c=cities[i].lower()
            if c not in city:
                if len(city)>=cacheSize:
                    city.pop(0)
                city.append(c)
                answer+=5
            else:
                city.remove(c)
                city.append(c)
                answer+=1
                
    else:  
        answer=5*len(cities)
    return answer