import sys
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

result=[]
for i in range(1,n):
    string=""
    val=gcd(arr[0],arr[i])
    string+=str(arr[0]//val)
    string+="/"
    string+=str(arr[i]//val)
    result.append(string)

for i in range(n-1):
    print(result[i])