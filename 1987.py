import sys
sys.setrecursionlimit(10000)

def dfs(r,c,v):
    global cnt
    cnt=max(cnt,v)

    for d in range(4):
        x,y=r+dx[d],c+dy[d]
        if 0<=x<n and 0<=y<m and not used[ord(board[x][y])-65]:
            used[ord(board[x][y])-65]=True
            dfs(x,y,v+1)
            used[ord(board[x][y])-65]=False

n,m=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
used=[False] * 26       
used[ord(board[0][0])-65]=True

cnt=1
dfs(0,0,1)
print(cnt)