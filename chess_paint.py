#체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
#하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
#입력으로 체스판의 높이(세로), 너비(가로)가 오고,
#잘못 색칠된 체스판을 입력해준다.

def white_chess():
    white = []
    for i in range(8):
        string = ""
        for j in range(8):
            if i%2 == 0:
                if j%2 == 0:
                    string += "W"
                else:
                    string += "B"
            else:
                if j%2 == 1:
                    string += "W"
                else:
                    string += "B"
        white.append(string)
    return white

def check(wrong,right):
    repaint = 0
    for i in range(8):
        for j in range(8):
            if wrong[i][j] != right[i][j]:
                repaint +=1
    return repaint

input_num = input().split()
sero = int(input_num[0])
garo = int(input_num[1])
chess = []
for i in range(sero):
    chess.append(input())

mini = 65
for i in range(sero-7):
    for j in range(garo-7):
        new = []
        for x in range(i,i+8):
            string = ""
            for y in range(j,j+8):
                string += chess[x][y]    
            new.append(string)
        
        if mini > min(check(new,white_chess()),64-check(new,white_chess())):
            mini = min(check(new,white_chess()),64-check(new,white_chess()))

print(mini)