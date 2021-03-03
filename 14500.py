import sys
n,m=map(int,sys.stdin.readline().split())
pap=[]
for _ in range(n): pap.append(list(map(int,sys.stdin.readline().split())))


def stick(i,j):
    global n,m
    garo,sero=0,0
    if i+3<n:
        for k in range(4): garo+=pap[i+k][j]
    if j+3<m:
        for k in range(4): sero+=pap[i][j+k]
    return max(sero,garo)

def box(i,j):
    global n,m
    total=0
    if i+1<n and j+1<m:
        total=pap[i][j]+pap[i+1][j]+pap[i][j+1]+pap[i+1][j+1]
    return total

def six(i,j):
    global n,m
    total=0
    maxi=0
    if i+2<n and j+1<m:
        for k in range(3):
            for l in range(2):
                total+=pap[i+k][j+l]
        maxi=total-min(pap[i][j]+pap[i+1][j],pap[i+1][j]+pap[i+2][j],pap[i][j+1]+pap[i+1][j+1],pap[i+1][j+1]+pap[i+2][j+1],pap[i][j]+pap[i+2][j],pap[i][j+1]+pap[i+2][j+1],pap[i][j]+pap[i+2][j+1],pap[i][j+1]+pap[i+2][j])
    return maxi

def garosix(i,j):
    global n,m
    total=0
    maxi=0
    if i+1<n and j+2<m:
        for k in range(3):
            for l in range(2):
                total+=pap[i+l][j+k]
        maxi=total-min(pap[i][j]+pap[i][j+1],pap[i][j+1]+pap[i][j+2],pap[i+1][j]+pap[i+1][j+1],pap[i+1][j+1]+pap[i+1][j+2],pap[i][j]+pap[i][j+2],pap[i+1][j]+pap[i+1][j+2],pap[i][j]+pap[i+1][j+2],pap[i+1][j]+pap[i][j+2])
    return maxi

maximum=0
for i in range(n):
    for j in range(m):
        maximum=max(maximum,stick(i,j),box(i,j),six(i,j),garosix(i,j))
print(maximum)