import sys
input = sys.stdin.readline

def binarySearch(l, r, val):
    global arr
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == val: return True
        elif arr[mid] < val: l = mid+1
        else: r = mid-1
    return False

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
search = list(map(int,input().split()))

for e in search:
    if binarySearch(0,N-1,e): print(1)
    else: print(0)