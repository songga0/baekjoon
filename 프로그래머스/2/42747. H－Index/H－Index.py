def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)
    m=max(citations)
    for i in range(m,0,-1):
        cnt=0
        for j in citations:
            if j>=i:
                cnt+=1
            else:
                break
        if cnt>=i:
            answer=i
            break
    return answer