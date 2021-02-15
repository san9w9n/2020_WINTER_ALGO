import sys
N=int(sys.stdin.readline())
fibolist=[0,1]+[-1]*39
def fibo(k):
    if k==0: return 0
    if k==1: return 1
    if fibolist[k]==-1:
        fibolist[k]=fibo(k-1) + fibo(k-2)
        return fibolist[k]
    else: return fibolist[k]
fibo(40)
for _ in range(N):
    T=int(sys.stdin.readline())
    if T==0: print("1 0")
    elif T==1: print("0 1")
    else:
        print("{} {}".format(fibolist[T-1],fibolist[T]))
