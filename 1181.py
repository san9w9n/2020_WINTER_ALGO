#문자열이 온다. heap 정렬을 써보자!

def heap(arr):
    #최대힙을 만들어야해요.
    n=len(arr)
    for i in range(n):
        c=i
        while c!=0:
            root = (c-1)//2
            if len(arr[root])<len(arr[c]):
                arr[root], arr[c] = arr[c], arr[root]
            elif len(arr[root])==len(arr[c]):
                if arr[root]<=arr[c]:
                    arr[root], arr[c] = arr[c], arr[root]
            c = root
    
    #최대힙을 이제 소트해줘요
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        c=1
        root=0
        while c<i:
            c = 2*root+1
            if c<i-1 and len(arr[c])<len(arr[c+1]): c+=1
            elif c<i-1 and len(arr[c])==len(arr[c+1]):
                if arr[c]<=arr[c+1]:
                    c+=1
            if c<i and len(arr[c])>len(arr[root]):
                arr[root], arr[c] = arr[c], arr[root]
            elif c<i and len(arr[c])==len(arr[root]):
                if arr[root]<=arr[c]:
                    arr[root], arr[c] = arr[c], arr[root]
            root=c



N = int(input())
arr=[]
for _ in range(N):
    arr.append(input())
arr=list(set(arr))
heap(arr)

for i in range(len(arr)):
    print(arr[i])