import sys
s=list(sys.stdin.readline().strip())

string=""
arr=[]
for i in range(len(s)):
    if s[i]=='+':
        arr.append(str(int(string)))
        arr.append('+')
        string=""  
    elif s[i]=='-':
        arr.append(str(int(string)))
        arr.append('-')
        string=""
    else:
        string+=s[i]
arr.append(str(int(string)))

sik=[]
string=""
for i in range(len(arr)):
    if arr[i]=='-':
        sik.append(eval(string))
        string=""
    else:
        string+=arr[i]
sik.append(eval(string))

sub=sik[0]
for i in range(1,len(sik)):
    sub-=sik[i]

print(sub)