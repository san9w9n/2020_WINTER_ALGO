import sys
def fac(n):
    if n==1: return 1
    return n*fac(n-1)

n=int(sys.stdin.readline())
if n==0:
    print(0)
    sys.exit(0)
a=str(fac(n))
cnt=0
for i in range(len(a)-1,0,-1):
    if a[i]!='0': break
    else: cnt+=1

print(cnt)

#원래 풀으려고 했던 방식은
#5을 찾으면 +1, 10을 찾으면 +1 이런 식이었다.
#그런데 25와 125를 생각을 못해서 답을 틀렸다.

#가장 효율적인 방법은
#print(N//5+N//25+N//125) 이다.