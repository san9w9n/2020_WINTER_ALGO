import sys

n = int(sys.stdin.readline())
guess = list(map(int,sys.stdin.readline().split()))
guess.sort()
m = int(sys.stdin.readline())
answer = list(map(int,sys.stdin.readline().split()))

#이진탐색
for i in answer:
    low,high,flag=0,n-1,0
    while low<=high:
        mid=(low+high)//2
        if guess[mid]==i:
            flag=1
            break
        elif guess[mid]<i:
            low=mid+1
        else:
            high=mid-1

    if flag==1:
        print(1,end=" ")
    else:
        print(0,end=" ")

    
