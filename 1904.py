import sys
n=int(sys.stdin.readline())
fibo=[0]*1000001
fibo[0]=1
fibo[1]=1
for i in range(2,n+1):
    fibo[i]=(fibo[i-2]+fibo[i-1])%15746
print(fibo[n])