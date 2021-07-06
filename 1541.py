import sys
input = sys.stdin.readline

line = input().strip()
op = []

i=0
string = ""
while i<len(line):
    try:
        c = int(line[i])
        string+=line[i]
    except:
        
        if string: op.append(int(string))
        string = ""
        if line[i]=="-": op.append(line[i])
    i+=1
if string: op.append(int(string))

total = 0
add = 0

for i in range(len(op)-1 , -1, -1):
    if op[i]=="-":
        total-=add
        add=0
    else: add+=op[i]
if add>0: total+=add

print(total)
    
    


