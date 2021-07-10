import sys
input = sys.stdin.readline

N = int(input())
arr = ['1', '2', '3']

def dfs(k, s, now):
    for i in range(1, (len(s)//2)+1):
        if s[-i:] == s[-2*i:-i]: return
    if len(s)==N:
            print(''.join(s))
            sys.exit(0)
    else:
        for i in range(3):
            if i!=now:
                s.append(arr[i])
                dfs(k+1,s,i)
                s.pop()
dfs(0,[],-1)
