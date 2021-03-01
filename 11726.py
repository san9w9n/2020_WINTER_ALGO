import sys
n=int(sys.stdin.readline())
#피보나치 수열을 만족하는 규칙
dp=[0,1,2]+[0]*(n-2)

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%10007)
