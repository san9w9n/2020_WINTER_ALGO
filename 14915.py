def hexa(arr):
    for i in range(len(arr)):
        if arr[i]=='10': arr[i]='A'
        elif arr[i]=='11': arr[i]='B'
        elif arr[i]=='12': arr[i]='C'
        elif arr[i]=='13': arr[i]='D'
        elif arr[i]=='14': arr[i]='E'
        elif arr[i]=='15': arr[i]='F'

def int_part(n,r):
    arr=[]
    string=""
    while n>=r:
        arr.append(str(n%r))
        n//=r
    arr.append(str(n))
    if r>=11: hexa(arr)
    for s in arr:
        string=s+string
    return string

n,r=map(int,input().split())

integer=int_part(n,r)

print(integer)
