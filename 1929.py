import sys
def isPrime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

A,B = map(int,sys.stdin.readline().split())
answer = []
for x in range(A,B+1):
    if isPrime(x):
        answer.append(x)

for x in answer:
    print(x)
    
            