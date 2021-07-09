import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs():
    global arr, dp
    x,y=0,0
    queue = deque([(x,y)])
    arr[x][y] = '0'

    while queue:
        x, y = queue.popleft()
        if x==N-1 and y==M-1:
            print(dp[x][y])
            break
        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if 0<=r<N and 0<=c<M:
                if dp[r][c] == 0 and arr[r][c] == '1':
                    dp[r][c] = dp[x][y] + 1
                    arr[r][c] = '0'
                    queue.append((r,c))

bfs()


