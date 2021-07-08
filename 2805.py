import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def binarysearch():
    l = 0
    r = max(arr)
    maxi = 0
    while l<=r:
        mid = (l+r)//2
        total = 0
        for e in arr:
            if mid<e: total+= e-mid
        if total<M: r = mid-1
        else:
            l = mid+1
            maxi = max(maxi,mid)
    return maxi

print(binarysearch())
