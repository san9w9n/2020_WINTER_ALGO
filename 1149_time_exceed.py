import sys
#시간초과가 난다.
#dp를 사용하지 않았기 때문인데, 순서하나하나를 리스트에
#저장하기가 힘들기 때문에 포기했다.
#for문을 사용한다면 한번만 들리기 때문에 편하게
#dp를 구현할 수 있다.
N=int(sys.stdin.readline())
cost=[]
for _ in range(N):
    cost.append(list(map(int,sys.stdin.readline().split())))
mini=1000*N
def paint(k,money,lastcolor):
    global mini
    if k>=N:
        mini=min(mini,money)
        return
    for i in range(3):
        if lastcolor!=i:
            paint(k+1,money+cost[k][i],i)
paint(0,0,-1)
print(mini)