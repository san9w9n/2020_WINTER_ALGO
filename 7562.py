import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

for _ in range(T):
    L = int(input())
    field = [[0 for _ in range(L)] for _ in range(L)]
    x, y = map(int, input().split())
    field[x][y] = 1
    tx, ty = map(int, input().split())

    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        if x==tx and y==ty: break
        for d in range(8):
            r, c = x+dx[d], y+dy[d]
            if 0<=r<L and 0<=c<L and field[r][c] == 0:
                field[r][c] = field[x][y] + 1
                queue.append((r,c))

    if field[tx][ty]>0: print(field[tx][ty] - 1)
    else: print(0)
