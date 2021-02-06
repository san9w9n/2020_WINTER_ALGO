import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())

n=10001
arr=[False, False] + [True] * (n-1)
prime=[]
for i in range(2,n+1):
    if arr[i]:
        prime.append(i)
    for j in range(2*i,n+1,i):
        arr[j]=False

total=0
mini=10001
for i in prime:
    if a <= i <= b:
        if mini>=i: mini=i 
        total+=i

if total==0: print(-1)
else:
    print(total)
    print(mini)
    