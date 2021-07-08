import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

vector = [arr[0]]

def lower(val):
    global vector
    l=0
    r=len(vector)-1
    mini = 1e9
    while l<=r:
        mid = (l+r)//2
        if vector[mid] >= val:
            r = mid-1
            mini = min(mini, mid)
        else: l = mid+1
    return mini

for e in arr[1:]:
    index = lower(e)
    if index>=len(vector): vector.append(e)
    else: vector[index] = e
print(len(vector))
    

