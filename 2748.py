import sys
n=int(sys.stdin.readline())
dp=[0,1,1]+[0]*n

def fibo(k):
    if k==1: return 1
    if k==2: return 1
    if dp[k]!=0: return dp[k]
    else:        
        dp[k]=fibo(k-1)+fibo(k-2)
        return dp[k]
fibo(n)
print(dp[n])