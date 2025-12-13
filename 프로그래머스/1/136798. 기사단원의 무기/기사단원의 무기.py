def solution(number, limit, power):
    answer=0
    pow = []
    for i in range(1,number+1):
        res=[]
        for j in range (1,int(i**0.5)+1):
            if i%j==0:
                res.append(j)
                if i==j*j:
                    continue
                else:
                    res.append(i//j)
        pow.append(len(res))
    for i in pow:
        if i<=limit:
            answer+=i
        else:
            answer+=power
    return answer