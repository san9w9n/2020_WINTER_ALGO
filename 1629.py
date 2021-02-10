import sys

def mod(a,m,n):
    #base
    if m==1: return a%n
    #m이 짝수
    val = mod(a,m//2,n)
    val = val * val % n
    if m%2==0: return val
    return val * a % n

a,m,n=map(int,sys.stdin.readline().split())
ans = mod(a,m,n)
print(ans)