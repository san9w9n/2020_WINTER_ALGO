#HeapSort, 힙정렬

def HeapSort(arr):

    #먼저 전체 트리 구조를 최대 힙 구조로 바꾼다.
    for i in range(1,len(arr)):
        c = i
        while c != 0:
            root = (c-1)//2
            if arr[root] < arr[c]:
                arr[root], arr[c] = arr[c], arr[root]
            c = root
    
    #크기를 줄여가며 반복적으로 힙을 구성
    for i in range(len(arr)-1, -1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        root = 0
        c = 1
        while c<i:
            c = 2 * root + 1
            if c < i-1 and arr[c] < arr[c+1]:
                c+=1 #더 큰 값을 찾음
            if c < i and arr[root] < arr[c]:
                arr[root], arr[c] = arr[c], arr[root]
            root = c

arr = list(map(int,input().split()))
HeapSort(arr)
print(arr)
