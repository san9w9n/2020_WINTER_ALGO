import sys
def func(n,arr):
    if n==1: return
    for i in range(len(arr)):
        if n//3<=i%n<2*(n//3):
            for j in range(len(arr)):
                if n//3<=j%n<2*(n//3):
                    arr[i][j]=' '
    func(n//3,arr)

N=int(sys.stdin.readline())
arr = [['*' for _ in range(N)] for _ in range(N)]

func(N,arr)
str = ''
for s in arr:
    print(*s, sep='')