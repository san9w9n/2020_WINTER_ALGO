import sys
from collections import deque

m,n=map(int,sys.stdin.readline().split())
visit=deque([])

box=[]
tomato=0
cnt=0
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if line[j]==1:
            cnt+=1
            tomato+=1
            visit.append((i,j))
        if line[j]==0: tomato+=1
    box.append(line)

if cnt==tomato:
    print(0)
    sys.exit(0)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
day=1
while True:
    for _ in range(len(visit)):
        x,y=visit.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
                box[nx][ny]=1
                cnt+=1
                visit.append((nx,ny))
    if cnt==tomato:
        print(day)
        break
    if day>n*m:
        print(-1)
        break
    day+=1   