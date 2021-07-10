import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(idx, total):
    global cnt
    if idx >= N:
        return
    total += arr[idx]
    if total == S:
        cnt += 1
    dfs(idx + 1, total - arr[idx])
    dfs(idx + 1, total)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
            

