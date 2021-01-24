#우리가 흔히 알고 있는 숫자야구 게임이다.
#그런데 이번엔 숫자를 맞추는 것이 아닌,
#정답으로 추측할 수 있는 숫자가 몇 개 인지 판단해야한다.

#스트라이크 체크 함수
def strike_check(guess,n):
    '''스트라이크를 체크 후 스트라이크 리턴,
    인자는 추측하는 수와 N_list에 있는 수를 받는다.'''
    strike = 0
    if(guess[0] == n[0]):
        strike+=1
    if(guess[1] == n[1]):
        strike+=1
    if(guess[2] == n[2]):
        strike+=1
        
    return strike

def ball_check(guess, n):
    '''볼 체크 후 볼 리턴,
    인자는 추측하는 수와 N_list에 있는 수를 받는다.'''
    ball = 0
    for i in range(3):
        if guess[i] != n[i] and guess[i] in n:
            ball+=1

    return ball


#그냥 숫자 123 부터 ~ 987 까지 배열 만들어서 거기서 하나하나 탐색하자
N_list = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if(i!=j and j!=k and i!=k):
                N_list.append(str(i*100 + j*10 + k))

#각 테스트 케이스들을 이중배열로 담는다. 체크하려는 숫자는 문자열로 하는게 편할 것 같다.
case = int(input())
arr = []
for _ in range(case):
    arr.append(list(map(int,input().split())))
for i in range(case):
    arr[i][0] = str(arr[i][0])


#이제 strike_check 함수와 ball_check 함수를 써서 카운트와 다르면 리스트에서 제거
new_list = []
for x in N_list:
    count = 0
    for i in range(case):
        if strike_check(arr[i][0],x)==arr[i][1] and ball_check(arr[i][0],x)==arr[i][2]:
            count+=1
    if count == case:
        new_list.append(x)

print(len(new_list))

