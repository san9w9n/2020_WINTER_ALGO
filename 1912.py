import sys
#1912_re 에서는 정답은 맞게 했지만, 
#또 계산하는 것을 버리지 못했다.
#즉, max(dp[i-1]+arr[i],arr[i]) 이 부분이 관건이었다.
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
dp=[arr[0]]
for i in range(1,n):
    dp.append(max(dp[i-1]+arr[i],arr[i]))
print(max(dp))