import sys
input = sys.stdin.readline

N, H = map(int,input().split())
upward = [-1] + [0] * H
downward = [-1] + [0] * H
up = [False] + [False] * H
down = [False] + [False] * H

for i in range(N):
    n = int(input())
    if i%2==0: #석순
        up[n] = True
        upward[n] += 1
    else: #종유석
        down[n] = True
        downward[n] += 1
        
for i in range(len(upward)-1, 1, -1):
    upward[i-1] += upward[i]
for i in range(len(downward)-1, 1, -1):
    downward[i-1] += downward[i]

dp = [0] + [0]*H

for i in range(1,H+1):
    dp[i]+=upward[i]
    dp[H-i+1]+=downward[i]


mini = min(dp[1:])
count = dp[1:].count(mini)

print(mini,count)