import sys
n,m,x,y,k=map(int,sys.stdin.readline().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
move=list(map(int,sys.stdin.readline().split()))
dice={1:0,2:0,3:0,4:0,5:0,6:0}

top=1
l=4
r=3
u=2
d=5
op=6
def east():
    global top,l,r,u,d,op
    temp=top
    top=l
    temp2=r
    r=temp
    l=op
    op=temp2

def west():
    global top,l,r,u,d,op
    temp=top
    top=r
    temp2=l
    l=temp
    r=op
    op=temp2

def south():
    global top,l,r,u,d,op
    temp=top
    top=d
    temp2=u
    u=temp
    d=op
    op=temp2

def north():
    global top,l,r,u,d,op
    temp=top
    top=u
    temp2=d
    d=temp
    u=op
    op=temp2

for s in move:
    if x+1<n and s==4:
        x+=1
        north()
        if arr[x][y]!=0:
            dice[op]=arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[op]
        print(dice[top])
    elif x-1>=0 and s==3:
        x-=1
        south()
        if arr[x][y]!=0:
            dice[op]=arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[op]
        print(dice[top])
    elif y-1>=0 and s==2:
        y-=1
        west()
        if arr[x][y]!=0:
            dice[op]=arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[op]
        print(dice[top])
    elif y+1<m and s==1:
        y+=1
        east()
        if arr[x][y]!=0:
            dice[op]=arr[x][y]
            arr[x][y]=0
        else:
            arr[x][y]=dice[op]
        print(dice[top])