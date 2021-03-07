import sys
n,b=map(int,sys.stdin.readline().split())
A=[]
for _ in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))

def mulmat(M1,M2):
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=M1[i][k]*M2[k][j]
            result[i][j]%=1000
    return result

def divmat(A,B):
    if B==1:
        for i in range(n):
            for j in range(n):
                A[i][j]%=1000
        return A
    elif B%2==1:
        matrix=divmat(A,B-1)
        new_mat=mulmat(A,matrix)

        return new_mat
    else:
        matrix=divmat(A,B//2)
        new_mat=mulmat(matrix,matrix)
        return new_mat

ans = divmat(A,b)

for row in ans:
    print(*row)
