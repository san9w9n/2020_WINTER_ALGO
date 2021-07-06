import sys
from collections import deque
input = sys.stdin.readline

# 기본 0, 사과는 1, 뱀은 8
N = int(input())
field = [[0 for _ in range(N)] for _ in range(N)]
field[0][0] = 8

K = int(input())
for _ in range(K):
    I, J = map(int, input().split())
    field[I-1][J-1] = 1

L = int(input())
direct_info = [0 for _ in range(10001)]
for _ in range(L):
    X, C = map(str, input().split())
    direct_info[int(X)] = C

def move_check(x,y, dx,dy):
    global field
    if(field[x+dx][y+dy] == 1):
        return 1
    elif(field[x+dx][y+dy] == 8):
        return -1
    else: return 0

def rotate(d,sec):
    global direct_info
    if direct_info[sec] == 0: return d
    elif direct_info[sec] == 'D':
        if d==0: return 3
        else: return d-1
    else:
        if d==3: return 0
        else: return d+1
    
def print_field():
    global field
    for r in field:
        print(*r)

def move():
    global field, N
    sec = 0
    d = 0
    x = 0
    y = 0
    # 동, 북, 서, 남으로 이동
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    info = deque([(0,0)])

    while True:
        sec+=1
        r = x+dx[d]
        c = y+dy[d]

        if 0<=r<N and 0<=c<N:
            check = move_check(x,y,dx[d],dy[d])
            if check == 1:
                x = r
                y = c
                field[x][y] = 8
                info.append((x,y))
            elif check == 0:
                p,q = info.popleft()
                field[p][q] = 0
                x = r
                y = c
                field[x][y] = 8
                info.append((x,y))

            else: break
        else: break

        d = rotate(d,sec)
        
    return sec


print(move())