import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visit = [True] + [False] * N

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(k):
    queue = deque([k])
    visit[k] = True

    while queue:
        current = queue.popleft()
        visit[current] = True
        for e in arr[current]:
            if not visit[e]:
                queue.append(e)
                visit[e] = True
    
ans = 0
for i in range(1, N+1):
    if not visit[i]: 
        bfs(i)
        ans+=1

print(ans)