import sys
import math
up, down, high = map(int,sys.stdin.readline().split())

day = math.ceil((high-down)/(up-down))
print(day)