import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = sorted(list(input().strip().split()))
used = [False] * C

vow = 'aeiou'
def check(sol):
    mo = ja = 0
    for e in sol:
        if e in vow: mo+=1
        else: ja+=1
    return mo>=1 and ja>=2

def dfs(sol):
    if len(sol)==L and check(sol):
        print(''.join(sol))
    else:
        for i in range(C):
            if not used[i]:
                sol.append(alphabet[i])
                for j in range(0,i+1):
                    used[j] =True
                dfs(sol)
                sol.pop()
                for j in range(0,i+1):
                    used[j] = False
dfs([])

