import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

dp=[arr[0]]
maxi=arr[0]
for i in range(1,n):
    for j in range(1,i+1):
        dp[j-1]+=arr[i]
        m=max(dp)
        if maxi<=m: maxi=m
    dp.append(arr[i])
print(maxi)