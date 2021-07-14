from collections import deque
import sys, heapq
input = sys.stdin.readline
INF = 1e9


def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + graph[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def bfs():
    q = deque()
    q.append(d)
    while q:
        v = q.popleft()
        if v == s: continue
        for pre_v, pre_c in r_graph[v]:
            if distance[pre_v] + graph[pre_v][v] == distance[v]:
                if (pre_v, v) not in remove_List:
                    remove_List.append((pre_v, v))
                    q.append(pre_v)



while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    s, d = map(int, input().split())
    graph = [{} for _ in range(n)]
    r_graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        r_graph[v].append((u, p))

    distance = [INF] * n
    dijkstra()

    remove_List = []
    bfs()
    for u, v in remove_List:
        del graph[u][v]

    distance = [INF] * n
    dijkstra()
    if distance[d] == INF: print(-1)
    else: print(distance[d])