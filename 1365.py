import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
vector = [arr[0]]

def lower(val):
    global vector
    mini = 1e9
    l = 0
    r = len(vector)-1
    while l<=r:
        mid = (l+r)//2
        if vector[mid] >= val:
            mini = min(mini, mid)
            r = mid-1
        else: l = mid+1
    return mini

for e in arr[1:]:
    index = lower(e)
    if index>=len(vector): vector.append(e)
    else: vector[index] = e

print(len(arr) - len(vector))