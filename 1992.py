import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n): arr.append(list(sys.stdin.readline().rstrip()))
string=""
def func(k,pap):
    global string
    color=0
    
    for i in range(k):
        for j in range(k):
            if pap[i][j]=='1': color+=1
    if color==k*k:
        string+="1"
        return
    elif color==0:
        string+="0"
        return
    else:
        string+="("
        func(k//2,[r[:k//2] for r in pap[:k//2]])
        func(k//2,[r[k//2:] for r in pap[:k//2]])
        func(k//2,[r[:k//2] for r in pap[k//2:]])
        func(k//2,[r[k//2:] for r in pap[k//2:]])
        string+=")"
func(n,arr)
print(string)
         

    