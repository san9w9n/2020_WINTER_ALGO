import sys

def check(N,arr):
    #최대힙 만들기
    for i in range(1,N):
        c=i
        while c!=0:
            root = (c-1)//2
            #y좌표가 더 크면 바로 바꿈
            if arr[root][1] < arr[c][1]:
                arr[root], arr[c] = arr[c], arr[root]
            #y좌표 같을 때, x좌표가 더 크면 바꿈
            elif arr[root][1]==arr[c][1] and arr[root][0] < arr[c][0]:
                arr[root], arr[c] = arr[c], arr[root]
            c = root
    #힙 정렬 시작
    for i in range(N-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        c=1
        root=0
        while c<i:
            c = 2*root+1
            if c<i-1 and arr[c][1] < arr[c+1][1]:
                c+=1
            elif c<i-1 and arr[c][1] == arr[c+1][1] and arr[c][0] < arr[c+1][0]:
                c+=1
            if c<i and arr[c][1] > arr[root][1]:
                arr[root], arr[c] = arr[c], arr[root]
            elif c<i and arr[c][1] == arr[root][1] and arr[c][0] > arr[root][0]:
                arr[root], arr[c] = arr[c], arr[root]
            root = c

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
check(N,arr)
for i in range(N):
    print("{} {}".format(arr[i][0], arr[i][1]))