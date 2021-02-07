import sys

n=5081
prime=[False,False]+[True]*(n+1)
for x in range(2,n+1):
    for y in range(2*x,n+1,x):
        prime[y]=False


T=int(sys.stdin.readline())
for _ in range(T):
    num=int(sys.stdin.readline())
    for i in range(num//2,1,-1):
        if prime[i]:
            if prime[num-i]:
                print("{} {}".format(i,num-i))
                break
                    