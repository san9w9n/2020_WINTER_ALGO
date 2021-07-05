import sys
sys.setrecursionlimit(10000)

n, b = map(int, sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def matrix(arr1, arr2):
    global n
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] = ret[i][j] + arr1[i][k] * arr2[k][j]
                ret[i][j] %= 1000
    return ret

def solve(arr, b):
    global n
    if b==1: 
        for i in range(n):
            for j in range(n):
                arr[i][j]%=1000
        return arr
    elif b%2 == 0: 
        mat = solve(arr, b//2)
        return matrix(mat,mat)
    else: return matrix(solve(arr, b-1), arr)

for row in solve(arr,b):
    print(*row)

    



