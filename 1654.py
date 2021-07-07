import sys
input = sys.stdin.readline

K, N = map(int, input().split())

maxi = 0
arr = []
for _ in range(K):
    n = int(input())
    maxi = max(maxi, n)
    arr.append(n)

def binarysearch():
    maxleng = 0
    low = 1
    high = maxi
    while low<=high:
        mid = (low+high)//2
        total = 0
        for e in arr:
            total+=e//mid
        if total<N: high = mid-1
        else:
            maxleng = max(maxleng, mid)
            low = mid+1
    return maxleng
print(binarysearch())



