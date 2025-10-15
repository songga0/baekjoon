def solution(m, n, puddles):
    #출발점 0,0 ,목적지 (n-1),(m-1)
    if [1,1] in puddles:
        return 0
    answer=0
    grid=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puddles:
                grid[i][j]=0
            else:
                grid[i][j]=1
    dp=[[0 for _ in range(m)] for _ in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                dp[i][j]=0
                continue
            if i>0:
                dp[i][j]+=dp[i-1][j]
            if j>0:
                dp[i][j]+=dp[i][j-1]
                
    return dp[n-1][m-1]%1000000007