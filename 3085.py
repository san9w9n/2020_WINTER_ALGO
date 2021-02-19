import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    line=list(sys.stdin.readline())
    arr.append(line[:n])

#세로줄 최대 연속 return
def con_sero(n,j):
    count=1
    m=1
    for i in range(n-1):
        if arr[i][j]==arr[i+1][j]:
            count+=1
        else: count=1
        m=max(m,count)
    return m
#가로줄 최대 연속 return
def con_garo(n,i):
    count=1
    m=1
    for j in range(n-1):
        if arr[i][j]==arr[i][j+1]:
            count+=1
        else: count=1
        m=max(m,count)
    return m
#교체 함수, 한번 더 사용하면 원래대로 돌리는 함수
def swap(x,y,i,j):
    arr[x][y],arr[i][j]=arr[i][j],arr[x][y]
    return
 
def garo(n):
    maxi=0
    for i in range(n-1):
        for j in range(n):
            swap(i,j,i+1,j)
            m=max(con_garo(n,i),con_garo(n,i+1),con_sero(n,j))
            maxi=max(maxi,m)  
            swap(i,j,i+1,j)
    return maxi

def sero(n):
    maxi=0
    for j in range(n-1):
        for i in range(n):
            swap(i,j,i,j+1)
            m=max(con_garo(n,i),con_sero(n,j),con_sero(n,j+1))
            maxi=max(maxi,m)
            swap(i,j,i,j+1)
    return maxi

maximum=max(garo(n),sero(n))
print(maximum)