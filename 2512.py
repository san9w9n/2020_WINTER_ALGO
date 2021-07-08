import sys
input = sys.stdin.readline

N =int(input())
arr = list(map(int,input().split()))
M = int(input())

# O(N)
maxi = max(arr)

def binarysearch():
    maxi_m = 0
    l = 0
    r = maxi
    while l<=r:
        mid = (l+r)//2
        total = 0
        for e in arr:
            if e<=mid: total+=e
            else: total+=mid
        
        if M>=total:
            maxi_m = max(maxi_m, mid)
            l = mid+1
        else:
            r = mid-1
    return maxi_m

print(binarysearch())
