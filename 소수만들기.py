import sys
sys.setrecursionlimit(10**6)

n=50000
a = [False,False] + [True]*(n-1)

for i in range(2,n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False

def bt(k,total,arr,isused):
    global answer
    if k==3:
        if a[total]:
            answer+=1
        return
    
    for i in range(len(arr)):
        if not isused[i]:
            for j in range(i+1):
                isused[j]=True
            bt(k+1,total+arr[i],arr,isused)
            for j in range(i+1):
                isused[j]=False

def solution(nums):
    global answer
    answer=0
    isused=[False]*len(nums)
    nums.sort()
    bt(0,0,nums,isused)

    return answer