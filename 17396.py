import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
canGo = list(map(int, input().split()))
canGo[-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

start = 0
target = N-1

def dijkstra():
    dist = [INF] * (N+1)
    heap = []

    heapq.heappush(heap, (0, start))
    while heap:
        d, now = heapq.heappop(heap)
        if dist[now] < d: continue
        for e in graph[now]:
            cost = e[1] + d
            if cost < dist[e[0]] and canGo[e[0]]==0:
                dist[e[0]] = cost
                heapq.heappush(heap, (cost, e[0]))
    if dist[target] == INF: return -1
    return dist[target]

print(dijkstra())
