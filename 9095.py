import sys
t=int(sys.stdin.readline())
#입력은 10까지 밖에 안들어오고,
#n>=4 일때, f(n)=f(n-3)+f(n-2)+f(n-1)의 규칙
dp=[0,1,2,4,7,13,24,44,81,149,274]
for _ in range(t):
    n=int(sys.stdin.readline())
    print(dp[n])
