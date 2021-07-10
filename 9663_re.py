import sys

N = int(sys.stdin.readline())
width = [False] * N
lcross = [False] * (2*N-1)
rcross = [False] * (2*N-1)

cnt = 0
def dfs(k):
    global cnt
    if k==N:
        cnt+=1
        return
    for i in range(N):
        if width[i] or lcross[k-i+N-1] or rcross[k+i]:
            continue
        width[i]=True
        lcross[k-i+N-1]=True
        rcross[k+i]=True
        dfs(k+1)
        width[i]=False
        lcross[k-i+N-1]=False
        rcross[k+i]=False
dfs(0)
print(cnt)