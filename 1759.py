import sys

l,c=map(int,sys.stdin.readline().split())
char=list(map(str,sys.stdin.readline().split()))
char.sort()
used=[False for _ in range(c)]
string=[]
ans=[]
def backtracking(k):
    if k==l:
        ans.append(''.join(map(str,string)))
        return
    for i in range(c):
        if not used[i]:
            string.append(char[i])
            for j in range(i+1):
                used[j]=True
            backtracking(k+1)
            string.pop()
            for j in range(i+1):
                used[j]=False

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

backtracking(0)
password(ans)
