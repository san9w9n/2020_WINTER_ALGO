import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def binarysearch():
    l = 1
    r = 100 * N
    ans = 1e9
    while l<=r:
        mid = (l+r)//2
        total = 0
        cnt = 1
        check = True
        for i in range(len(arr)):
            total+=arr[i]
            if arr[i]>mid:
                left=mid+1
                check=False
                break
            if total>mid:
                total=arr[i]
                cnt+=1
        if cnt>M or not check:
            l = mid+1
        else:
            r = mid-1
            ans = min(ans,mid)
    return ans

def printAns(mid):
    global M
    ans = []
    print(mid)
    cnt, total = 0, 0
    for i in range(len(arr)):
        total+=arr[i]
        if total>mid:
            total=arr[i]
            M-=1
            print(cnt, end=" ")
            cnt=0
        cnt+=1
        if N-i == M: break;
    while M-1>=0:
        print(cnt, end=" ")
        cnt = 1
        M-=1

printAns(binarysearch())