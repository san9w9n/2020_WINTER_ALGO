import sys

n,k=map(int,sys.stdin.readline().split())
s=[[0,0]]
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))

dp=[[0 for x in range(k+1)] for y in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= s[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-s[i][0]]+s[i][1])
        else:
            dp[i][j]=dp[i-1][j]
        
print(dp[n][k])