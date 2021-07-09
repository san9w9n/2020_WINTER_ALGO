import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
start, end = map(int, input().split())
M = int(input())
edge = [[] for _ in range(N+1)]
visit = [True] + [False] * N
dp = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

def bfs():
    queue = deque([start])
    visit[start] = True
    while queue:
        k = queue.popleft()
        if k==end: return dp[end]
        for e in edge[k]:
            if not visit[e]:
                queue.append(e)
                visit[e] = True
                dp[e] = dp[k] + 1
    return -1

print(bfs())
