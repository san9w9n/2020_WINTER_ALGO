import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

t1=[]
isused=[False]*N
def chemi(i,j): return arr[i][j]+arr[j][i]
def add_sub(team1,team2):
    sum1,sum2=0,0
    for i in range(int(N/2)):
        for j in range(i+1,int(N/2)):
            sum1+=chemi(team1[i],team1[j])
            sum2+=chemi(team2[i],team2[j])
    return abs(sum1-sum2)
def full_t2(team1):
    arr=[]
    for i in range(N):
        if i not in team1:
            arr.append(i)
    return arr


min_=1e9
def func(k,team1):
    global min_
    if k==int(N/2):
        team2=full_t2(team1)
        m=add_sub(team1,team2)
        if min_>=m: min_=m
        return
    for i in range(N):
        if not isused[i]:
            team1.append(i)
            for j in range(i+1):
                isused[j]=True
            func(k+1,team1)
            for j in range(i+1):
                isused[j]=False
            team1.pop(-1)

func(0,t1)
print(min_)