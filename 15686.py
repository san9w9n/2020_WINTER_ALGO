import sys
from itertools import combinations

def dis(to,go):
    return abs(to[0]-go[0])+abs(to[1]-go[1])

n,m=map(int,sys.stdin.readline().split())
store=[]
home=[]
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if line[j]==1: home.append((i,j))
        elif line[j]==2: store.append((i,j))

arr=[[0 for x in range(len(store))] for y in range(len(home))]
comb=list(combinations([x for x in range(len(store))],m))

for i in range(len(home)):
    for j in range(len(store)):
        arr[i][j]=dis(home[i],store[j])

total_mini=1e9
for j in range(len(comb)):
    total=0
    for i in range(len(home)):
        mini=120
        for k in range(m):
            mini=min(mini,arr[i][comb[j][k]])
        total+=mini
    total_mini=min(total,total_mini)
            
print(total_mini)