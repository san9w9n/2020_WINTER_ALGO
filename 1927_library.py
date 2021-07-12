import heapq, sys
input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num==0:
        try: print(heapq.heappop(heap))
        except: print(0)
    else:
        heapq.heappush(heap,num)