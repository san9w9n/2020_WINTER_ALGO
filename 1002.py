import sys
t = int(sys.stdin.readline())
for _ in range(t):
    arr =list(map(int,sys.stdin.readline().split()))
    #점이 무한대(터렛이 같은 위치에있음)
    if arr[0]==arr[3] and arr[1]==arr[4] and arr[2]==arr[5]:
        print(-1)
    #점이 0개. 접한 거보다 멀 때
    elif (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2 > (arr[2]+arr[5])**2:
        print(0)
    #점이 0개. 안에서 접한거보다 가까울 때
    elif (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2 < (arr[2]-arr[5])**2:
        print(0)
    #점이 1개. 밖에서 접할때
    elif (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2 == (arr[2]+arr[5])**2:
        print(1)
    #점이 1개. 안에서 접할때
    elif (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2 == (arr[2]-arr[5])**2:
        print(1)
    #점이 2개. 겹칠 때
    elif (arr[0]-arr[3])**2 + (arr[1]-arr[4])**2 < (arr[2]+arr[5])**2:
        print(2)