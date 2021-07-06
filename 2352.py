import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
vector = []

def lower(val):
    global vector

    l,r = 0,len(vector)-1
    while l<=r:
        mid = (l+r)//2
        if vector[mid] > val: r = mid-1
        else: l = mid+1
    return l

for e in arr:
    if not vector or vector[-1] < e: vector.append(e)
    else: vector[lower(e)] = e

print(len(vector))