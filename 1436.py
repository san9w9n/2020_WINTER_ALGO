import sys

N=int(sys.stdin.readline())
num=666
while N>0:
    if str(num).find("666")!=-1: N-=1
    if N>0: num+=1
print(num)