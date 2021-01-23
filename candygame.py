#애니팡 게임이랑 똑같다. 첫줄에 N x N 게임판을 만들기 위해 N을 입력 받고,
#게임판을 준다. 여기서 인접한 서로 다른 사탕의 위치를 바꿔서 같은 사탕끼리
#한 열에 있을 때 그 사탕을 먹을 수 있다. 이때 최대로 먹을 수 있는 사탕의 수
#사탕의 종류는 4개가 있다.

#입력받는 함수
def input_game():
    N = int(input())
    game = []
    for _ in range(N):
        game.append(list(map(str, input())))

    return N, game


def garo_serial(num,arr):
    '''가로줄에서 연속된 거 찾는 함수, 인자는 배열전체를 받는다.'''
    serial = 0
    length = num
    max = 0
    for j in range(length):
        serial = 0
        for i in range(length):
            if i < length-1 and arr[j][i] == arr[j][i+1]:
                serial += 1
            elif i < length-1 and arr[j][i] != arr[j][i+1]:
                break
        if max < serial: max = serial
    return max

def up_down(num,arr):
    '''윗줄 아랫줄 바꿔서 찾고 다시 원래 배열로 바꿔주기, 인자는 배열 전체'''
    max = 0
    
    for j in range(num):
        for i in range(num-1):
            temp1 = arr[i][j]
            arr[i][j] = arr[i+1][j]
            if max < sero_serial(num, arr):
                max = sero_serial(num, arr)
            if max < garo_serial(num,arr):
                max = garo_serial(num,arr)
        
            arr[i+1][j] = arr[i][j]
            arr[i][j] = temp1
    for i in range(num):
        for j in range(num):
            if i < num-1 and j < num-1:
                #바꿔주기
                temp = arr[i][j+1]
                arr[i][j+1] = arr[i+1][j+1]
                arr[i+1][j+1] = temp

                #다시 원래대로
                arr[i+1][j+1] = arr[i][j+1]
                arr[i][j+1] = temp
                if max < garo_serial(num,arr):
                    max = garo_serial(num,arr)

                if max < sero_serial(num, arr):
                    max = sero_serial(num, arr)
    return max+1

def sero_serial(num,arr):
    '''세로줄에서 연속된 거 찾아서 최고 연속 리턴 함수, 인자는 배열 전체를 받는다.'''
    max = 0
    length = num
    for j in range(length):
        serial = 0
        for i in range(length-1):
            if arr[i][j] == arr[i+1][j]:
                serial += 1
                if max < serial: max = serial
            else:
                break
    return max

def side(num, arr):
    '''양옆줄 바꿔서 연속된 거 찾고 다시 원래대로 바꿈'''
    max = 0
    for j in range(num):
        for i in range(num-1):
            temp = arr[j][i]
            arr[j][i] = arr[j][i+1]
            if max < sero_serial(num, arr):
                max = sero_serial(num, arr)
            if max < garo_serial(num, arr):
                max = garo_serial(num, arr)
            arr[j][i+1] = arr[j][i]
            arr[j][i] = temp

    for j in range(num-1):
        for i in range(num-1):
            temp = arr[i+1][j]
            arr[i+1][j] = arr[i+1][j+1]
            arr[i+1][j+1] = temp

            if max < sero_serial(num, arr):
                max = sero_serial(num,arr)
            if max < garo_serial(num,arr):
                max = garo_serial(num,arr)
            
            arr[i+1][j+1] = arr[i+1][j]
            arr[i+1][j] = temp
    
    return max+1
#main함수
num,array = input_game()
garo = up_down(num, array)
sero = side(num, array)

print(max(garo, sero))