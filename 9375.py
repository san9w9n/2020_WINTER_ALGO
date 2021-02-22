import sys
T=int(sys.stdin.readline())

def C(dic):
    arr=list(dic.keys())
    mul=1
    for i in arr:
        mul*=len(dic.get(i))+1
    return mul-1

for _ in range(T):
    N=int(sys.stdin.readline())
    closet={}
    for _ in range(N):
        a,b=map(str,sys.stdin.readline().split())
        if closet.get(b)==None:
            closet[b]=[a]
        else:
            closet[b].append(a)
    print(C(closet))
    closet.clear()
