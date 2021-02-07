import sys
def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


N = int(sys.stdin.readline())
answer = []
if N==1:
    print("")
else:
    while True:
        if not isprime(N):
            for x in range(2,N):
                if isprime(x) and N%x==0:
                    answer.append(x)
                    N=N//x
                    break
        else:
            answer.append(N)
            break
    for i in answer:
        print(i)

                