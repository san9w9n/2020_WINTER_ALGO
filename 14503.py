import sys
n,m=map(int,sys.stdin.readline().split())
r,c,d=map(int,sys.stdin.readline().split())
room=[]
di=[(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().split())))


clean=0
back=0
while True:
    if room[r][c]==0: clean,room[r][c]=clean+1,2
    #왼쪽 탐색
    while True:
        if back==4: break
        d=(d+3)%4
        if room[r+di[d][0]][c+di[d][1]]==0:
            r+=di[d][0]
            c+=di[d][1]
            back=0
            break
        else: back+=1
    if back==4:
        #사방이 둘러싸여 있을때 처리
        if room[r+di[(d+2)%4][0]][c+di[(d+2)%4][1]]==2:
            back=0
            r+=di[(d+2)%4][0]
            c+=di[(d+2)%4][1]
        elif room[r+di[(d+2)%4][0]][c+di[(d+2)%4][1]]==1: break
        
print(clean)
    

