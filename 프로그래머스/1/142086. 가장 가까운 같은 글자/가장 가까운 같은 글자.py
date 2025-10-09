def solution(s):
    answer = []
    for i in range(len(s)):
        if i==0:
            answer.append(-1)
        else:
            if s[i] not in s[:i]:
                answer.append(-1)
            else:
                cnt=0
                for j in range(i-1,-1,-1):
                    cnt+=1
                    if s[i]==s[j]:
                        answer.append(cnt)
                        break
    return answer