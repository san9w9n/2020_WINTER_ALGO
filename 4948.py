import sys

n=246912
prime=[0,0]+[1]*(n-1)
for x in range(2,n+1):
    for y in range(2*x, n+1, x):
        prime[y] = 0

while True:
    count=0
    num = int(sys.stdin.readline())
    if num==0: break
    for x in range(num+1,2*num+1):
        if prime[x]==1:
            count+=1
    print(count)