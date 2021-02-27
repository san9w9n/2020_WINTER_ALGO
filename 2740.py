import sys
arr1=[]
arr2=[]
n,m=map(int,sys.stdin.readline().split())
for _ in range(n): arr1.append(list(map(int,sys.stdin.readline().split())))
m,k=map(int,sys.stdin.readline().split())
for _ in range(m): arr2.append(list(map(int,sys.stdin.readline().split())))

res=[[0 for x in range(k)] for y in range(n)]

for i in range(m):
    for j in range(n):
        for l in range(k):
            res[j][l]+=arr1[j][i]*arr2[i][l]

for line in res:
    print(*line)