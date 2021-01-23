#분해합. a라는 숫자와 a 각 자리의 숫자를 합해서 나온 값이 b라고 하면,
#a는 b의 생성자이다.
#b의 입력으로 문제가 시작되며, 1부터 100만 까지 입력될 수 있다.
#우리는 가장 작은 a를 구해야한다.

to_num = int(input())
fromnum = 0


def checknum(from_num):
    '''from_num을 자리수마다 분해해서 sum함수를 사용해서 자리수의 합을 구하고
    그 값을 from_num과 더해서 생성자를 구하는 함수이다.
    '''
    arr = [] #배열 초기화. 안하면 그 전 횟수 차 거에서 계속 추가됨.
    
    #자리수 분해
    for i in str(from_num):
        arr.append(int(i))

    #자리수의 합과 원라 숫자와의 합을 to_num과 비교
    if from_num + sum(arr) == to_num:
        print(fromnum)
        return False #while 문에서 빠져나가기 위해서
    else: return True #while 문을 계속 돌기 위해서

while checknum(fromnum):
    fromnum += 1 #1부터 계속 돈다.
    if fromnum > to_num: #생성자는 분해합보다 커질 수 없으므로.
        print(0)
        break