from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for order in permutations(dungeons, len(dungeons)): 
        x=k
        cnt=0
        for i in order:
            if x>=i[0]:
                cnt+=1
                x-=i[1]
            else:
                break
        answer=max(answer,cnt)
    return answer