#A는 거꾸로 배열
#B는 정배열하면 된다.
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()
B.reverse()
total=0
for i in range(N):
    total += A[i] * B[i]

print(total)