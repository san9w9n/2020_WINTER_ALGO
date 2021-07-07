import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
maxi = 0
for _ in range(M): 
    n = int(input())
    arr.append(n)
    maxi = max(n,maxi)

def binarysearch():
    mini = 1e9
    l = 1
    r = maxi
    while l<=r:
        mid = (l+r)//2
        people = 0
        for e in arr:
            if e%mid==0: people+=e//mid
            else: people+=(e//mid) + 1
        if people<=N: 
            mini = min(mini, mid)
            r = mid-1
        else: l = mid+1

    return mini

print(binarysearch())