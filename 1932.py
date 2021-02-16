import sys
N=int(sys.stdin.readline())
tri=[]
for _ in range(N):
    tri.append(list(map(int,sys.stdin.readline().split())))
tri[1][0]+=tri[0][0]
tri[1][1]+=tri[0][0]

for i in range(2,N):
    for j in range(0,i+1):
        if j==0: tri[i][j]+=tri[i-1][0]
        elif j==i: tri[i][j]+=tri[i-1][j-1]
        else:
            tri[i][j]+=max(tri[i-1][j],tri[i-1][j-1])

print(max(tri[N-1]))