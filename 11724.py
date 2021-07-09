import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visit = [True] + [False] * N

for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(k):
    global visit
    visit[k] = True
    for e in arr[k]:
        if not visit[e]: dfs(e)


ans = 0
for i in range(1, N+1):
    if not visit[i]:
        dfs(i)
        ans+=1
print(ans)