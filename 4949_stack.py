import sys
#스택으로 풀어본 코드
while True:
    msg=sys.stdin.readline().rstrip()
    stack=[]
    if len(msg)==1 and msg[0]==".": break
    temp=True
    for c in msg:
        if c=="(" or c=="[":
            stack.append(c)
        elif c==")":
            if not stack or stack[-1]=="[":
                temp=False
                break
            elif stack[-1]=="(":
                stack.pop()
        elif c=="]":
            if not stack or stack[-1]=="(":
                temp=False
                break
            elif stack[-1]=="[":
                stack.pop()
    if temp==True and not stack:
        print("yes")
    else: print("no")