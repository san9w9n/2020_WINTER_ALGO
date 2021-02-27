import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N): arr.append(list(map(int,sys.stdin.readline().split())))
zero=0
one=0
minus=0
def f(k,pap):
    global zero,one,minus
    c1,c2,c3=0,0,0
    for i in range(k):
        for j in range(k):
            if pap[i][j]==0: c1+=1
            elif pap[i][j]==1: c2+=1
            elif pap[i][j]==-1: c3+=1
            if c1*c2!=0 or c2*c3!=0 or c2*c3!=0: break
    if c1==k*k:
        zero+=1
        return
    elif c2==k*k:
        one+=1
        return
    elif c3==k*k:
        minus+=1
        return
    else:
        f(k//3,[r[:k//3] for r in pap[:k//3]])        
        f(k//3,[r[:k//3] for r in pap[k//3:k//3*2]])
        f(k//3,[r[:k//3] for r in pap[k//3*2:]])
        f(k//3,[r[k//3:k//3*2] for r in pap[:k//3]])        
        f(k//3,[r[k//3:k//3*2] for r in pap[k//3:k//3*2]])
        f(k//3,[r[k//3:k//3*2] for r in pap[k//3*2:]])
        f(k//3,[r[k//3*2:] for r in pap[:k//3]])        
        f(k//3,[r[k//3*2:] for r in pap[k//3:k//3*2]])
        f(k//3,[r[k//3*2:] for r in pap[k//3*2:]])
f(N,arr)  
print(minus)
print(zero)
print(one)