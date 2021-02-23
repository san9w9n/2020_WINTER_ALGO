import sys

def f(s):
    if len(s)%2==1: return False
    while True:
        if len(s)==0: return True
        if "[]" in s:
            i=s.index("[]")
            s=s[:i]+s[i+2:]
        elif "()" in s:
            i=s.index("()")
            s=s[:i]+s[i+2:]
        else:
            return False

while True:
    msg=sys.stdin.readline().rstrip(".").split(".")[0]
    if len(msg)==0: break
    s=""
    for i in msg:
        if i=="(" or i==")" or i=="[" or i=="]":
            s+=i
    if f(s): print("yes")
    else: print("no")

