def solution(progresses, speeds):
    answer = []
    days=[]
    for i in range(len(progresses)):
        x=(100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]>0:
            x+=1
        days.append(x)
    d=days[0]
    cnt=1
    for i in range(1,len(days)):
        if days[i]<=d:
            cnt+=1
        else:
            answer.append(cnt)
            d=days[i]
            cnt=1
        if i==len(days)-1:
            answer.append(cnt)
    return answer
#[5,10,1,1,20,1]