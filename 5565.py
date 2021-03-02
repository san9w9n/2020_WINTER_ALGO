import sys
t=int(sys.stdin.readline())
for _ in range(9):
    n=int(sys.stdin.readline())
    t-=n
print(t)