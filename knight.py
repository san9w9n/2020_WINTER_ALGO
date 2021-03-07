import sys

m=list(sys.stdin.readline().rstrip())
char='abcdefgh'
r=int(m[1])-1
c=char.index(m[0])
move=[(2,1),(-2,1),(2,-1),(-1,-2)]
cnt=0

def can():
    global r,c,cnt
    for i in range(4):
        if 0 <= r+move[i][0] < 8 and 0 <= c+move[i][1] < 8: cnt+=1 
        if 0 <= r+move[i][1] < 8 and 0 <= c+move[i][0] < 8: cnt+=1

can()
print(cnt)