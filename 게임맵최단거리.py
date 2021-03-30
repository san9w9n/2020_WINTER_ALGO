from collections import deque
import copy
def solution(maps):
    answer=-1
    visited = copy.deepcopy(maps)
    n=len(maps)
    m=len(maps[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    que=deque([(0,0)])
    visited[0][0]=0
    while que:
        x,y=que.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]!=0:
                que.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1
                visited[nx][ny]=0
                
    if maps[n-1][m-1]!=1: answer=maps[n-1][m-1]
        
    return answer