import sys
arr=[]
for _ in range(9):
    arr.append(list(map(int,sys.stdin.readline().split())))
zero = [(i,j) for i in range(9) for j in range(9) if arr[i][j]==0]

def garofind(val,i):
    if val in arr[i]:
        return False
    return True

def serofind(val,j):
    for i in range(9):
        if val == arr[i][j]:
            return False
    return True

def three_three(val,i,j):
    ni,nj=i//3*3,j//3*3
    for x in range(3):
        for y in range(3):
            if val==arr[ni+x][nj+y]:
                return False
    return True

def func(k):
    if k == len(zero):
        for row in arr:
            for n in row:
                print(n,end=" ")
            print()
        sys.exit(0) #여러 개 중 하나만 출력.
    else:
        for i in range(1,10):
            x,y=zero[k][0],zero[k][1]
            if garofind(i,x) and serofind(i,y) and three_three(i,x,y):
                arr[x][y]=i
                func(k+1)
                arr[x][y]=0
            
func(0)