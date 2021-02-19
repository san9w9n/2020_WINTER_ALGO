import sys
a=list(sys.stdin.readline())
b=list(sys.stdin.readline())
a.pop(-1)
b.pop(-1)
la=len(a)
lb=len(b)
dp=[[0 for x in range(lb+1)] for y in range(la+1)]
for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
        