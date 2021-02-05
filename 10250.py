import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    h, w, n = map(int,sys.stdin.readline().split())
    high = n%h
    if high == 0: high = h
    width = math.ceil(n/h)
    print(high*100 + width)