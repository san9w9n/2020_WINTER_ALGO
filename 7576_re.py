import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
must = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 1: queue.append((i,j))
        elif field[i][j] == 0: must+=1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global queue
    length = len(queue)
    ans = 0
    color = 0
    while queue:
        x, y = queue.popleft()
        length-=1
        for d in range(4):
            r = x + dx[d]
            c = y + dy[d]
            if 0<=r<N and 0<=c<M and field[r][c]==0:
                field[r][c] = 1
                color+=1
                queue.append((r,c))
        if length==0 and queue:
            length = len(queue)
            ans+=1
    if color!=must: return -1
            
    return ans

print(bfs())




