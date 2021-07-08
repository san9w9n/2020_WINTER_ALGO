import sys
input = sys.stdin.readline
    
def lower(vector, val):
    l = 0
    r = len(vector)-1
    mini = 1e9
    while l<=r:
        mid = (l+r)//2
        if vector[mid] >= val:
            mini = min(mini,mid)
            r = mid-1
        else: l = mid+1
    return mini
while True:
    try:
        N = int(input())
        arr = list(map(int, input().split()))
        vector = [arr[0]]
        for e in arr[1:]:
            index = lower(vector, e)
            if index>=len(vector): vector.append(e)
            else: vector[index] = e
        print(len(vector))
    except:
        break