snail=[]
def down(i,j,n):
    while i+1<n and snail[i+1][j]==-1:
        snail[i+1][j]=snail[i][j]+1
        i+=1
    return i,j

def right(i,j):
    while j+1<=i and snail[i][j+1]==-1:
        snail[i][j+1]=snail[i][j]+1
        j+=1
    return i,j

def up(i,j):
    while snail[i-1][j-1]==-1:
        snail[i-1][j-1]=snail[i][j]+1
        i-=1
        j-=1
    return i,j

def solution(n):
    global snail
    answer = []
    i,j=0,0
    snail=[[-1 for _ in range(n)] for _ in range(n)]
    snail[0][0]=1
    
    count=0
    while count!=(n*(n+1))//2:
        i,j=down(i,j,n)
        i,j=right(i,j)
        i,j=up(i,j)
        count+=1

    for i in range(n):
        for j in range(i+1):
            answer.append(snail[i][j])
    return answer