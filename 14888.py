import sys
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
add,sub,mul,div=map(int,sys.stdin.readline().split())
max_=-(10**9)
min_=10**9
def func(k,res,add,sub,mul,div):
    global max_,min_
    if k==N:
        max_=max(res,max_)
        min_=min(res,min_)
        return
    if add:
        func(k+1,res+num[k],add-1,sub,mul,div)
    if sub:
        func(k+1,res-num[k],add,sub-1,mul,div)
    if mul:
        func(k+1,res*num[k],add,sub,mul-1,div)
    if div:
        func(k+1,int(res/num[k]),add,sub,mul,div-1)    


func(1,num[0],add,sub,mul,div)
print(max_)
print(min_)