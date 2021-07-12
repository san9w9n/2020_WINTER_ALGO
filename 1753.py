import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
dist = [1e9] * (V+1)
visit = [True] + [False] * V

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra():
    global dist
    heap = []
    heapq.heappush(heap, (0,start))
    dist[start] = 0
    while heap:
        d, now = heapq.heappop(heap)
        if visit[now]: continue
        visit[now] = True

        for e in graph[now]:
            cost = d + e[1]
            if dist[e[0]] > cost:
                dist[e[0]] = cost
                heapq.heappush(heap, (cost, e[0]))

dijkstra()

for i in range(1,V+1):
    if dist[i] == 1e9: print("INF")
    else: print(dist[i])



