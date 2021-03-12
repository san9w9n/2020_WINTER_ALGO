import sys, copy
from collections import deque

n,m=map(int,sys.stdin.readline().split())
board=[]
virus=deque([])
zero=0

for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        if line[j]==0: zero+=1
    board.append(line)

#벽 세개를 제외하고, 안전지역이 될 수 있는 수.
zero-=3
temp=copy.deepcopy(virus)
tmp=copy.deepcopy(board)


dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=0
def bfs():
    global board,virus,result
    infect=0
    copy = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = board[i][j]
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                virus.append((i, j))

    while virus:
        x,y=virus.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and copy[nx][ny]==0:
                infect+=1
                copy[nx][ny]=2
                virus.append((nx,ny))

    result=max(result,zero-infect)

def make_wall(k):
    global cnt
    if k==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                make_wall(k+1)
                board[i][j]=0
make_wall(0)
print(result)


