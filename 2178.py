import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
maze=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
dp=[[0 for _ in range(m)] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

visit=deque([(0,0)])
dp[0][0]=1

while visit:
    x,y=visit.popleft()
    print("구분")
    for line in dp:
        print(*line)
    if x==n-1 and y==m-1:
        print(dp[x][y])
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if dp[nx][ny]==0 and maze[nx][ny]=="1":
                dp[nx][ny] = dp[x][y] + 1
                visit.append((nx,ny))