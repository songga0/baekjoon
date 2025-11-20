
def solution(user_id, banned_id):
    answer = 0
    ban=[]
    for i in banned_id:
        x=[]
        for j in user_id:
            check=True
            if len(i)!=len(j):
                continue
            for ii,jj in zip(i,j):
                if ii=='*':
                    continue
                else:
                    if ii!=jj:
                        check=False
                        break
            if check:
                x.append(j)
        ban.append(x)
    s=set()
    def dfs(idx,user):
        if idx==len(banned_id):
            s.add(frozenset(user))
            return
        for b in ban[idx]:
            if b not in user:
                dfs(idx+1, user + [b])
    dfs(0, [])
    return len(s)