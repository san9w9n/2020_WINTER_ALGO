import sys
s=list(sys.stdin.readline().rstrip())
char=[]
total=0
for i in s:
    if i.isnumeric(): total+=int(i)
    else: char.append(i)
char.sort()

string=""
for s in char:
    string+=s

print(f"{string}{total}")