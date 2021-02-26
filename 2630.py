import sys

n=int(sys.stdin.readline())
arr=[]
for _ in range(n): arr.append(list(map(int,sys.stdin.readline().split())))

blue=0
white=0
def paper(k,pap):
    global blue,white
    color=0
    brk=0
    for i in range(k):
        for j in range(k):
            if pap[i][j]==1: color+=1
    if color==k*k:
        blue+=1
        return
    elif color==0:
        white+=1
        return
    else:
        paper(k//2,[r[:k//2] for r in pap[:k//2]])
        paper(k//2,[r[k//2:] for r in pap[:k//2]])
        paper(k//2,[r[:k//2] for r in pap[k//2:]])
        paper(k//2,[r[k//2:] for r in pap[k//2:]])
paper(n,arr)
print(white)
print(blue)