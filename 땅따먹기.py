def solution(land):
    now=-1
    dp=[[0 for _ in range(4)] for _ in range(len(land))]
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j!=k:
                    if i==1:
                        dp[i][j]=max(dp[i][j],land[i][j]+land[i-1][k])
                    else:
                        dp[i][j]=max(dp[i][j],land[i][j]+dp[i-1][k])
                    
    return max(dp[len(land)-1])