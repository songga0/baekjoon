def solution(genres, plays):
    g = []
    for i in genres:
        if [i,0] not in g:
            g.append([i,0])
    for i,j in zip(genres,plays):
        for k in g:
            if k[0]==i:
                k[1]+=j
                break
    g.sort(key=lambda x: x[1], reverse=True)
    index=[i for i in range(len(genres))]
    song=[]
    for i,j,k in zip(genres,plays,index):
        song.append([i,j,k])
    song.sort(key=lambda x: (-x[1],x[2]))
    answer=[]
    for i in g:
        cnt=0
        for j in song:
            if cnt==2:
                break
            if j[0]==i[0]:
                answer.append(j[2])
                cnt+=1
    return answer
