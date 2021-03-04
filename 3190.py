import sys
from collections import deque
n=int(sys.stdin.readline())
game=[[0 for x in range(n)] for y in range(n) ]

k=int(sys.stdin.readline())
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    game[x-1][y-1]=1

l=int(sys.stdin.readline())
move=[0 for x in range(10005)]
for _ in range(l):
    m=list(map(str,sys.stdin.readline().split()))
    m[0]=int(m[0])
    move[m[0]]=m[1]

r,c=0,0
game[0][0]=2
d=1
di=[(-1,0),(0,1),(1,0),(0,-1)] #북,동,남,서
game_over=0
snake=deque([(r,c)])
def die():
    global r,c,d
    if r+di[d][0]>=n or c+di[d][1]>=n or r+di[d][0]<0 or c+di[d][1]<0:
        return True
    elif game[r+di[d][0]][c+di[d][1]]==2:
        return True
    return False

def go():
    global r,c,d,game_over
    if die():
        game_over=1
        return
    elif not die() and game[r+di[d][0]][c+di[d][1]]==1:
        r+=di[d][0]
        c+=di[d][1]
        snake.append((r,c))
        game[r][c]=2
    elif not die() and game[r+di[d][0]][c+di[d][1]]==0:
        game[snake[0][0]][snake[0][1]]=0
        snake.popleft()
        r+=di[d][0]
        c+=di[d][1]
        snake.append((r,c))
        game[r][c]=2
    
time=0
game[r][c]==2
while True:
    go()
    if game_over==1: break
    time+=1
    if move[time]=="L": d=(d+3)%4
    elif move[time]=="D": d=(d+1)%4

print(time+1)


    

