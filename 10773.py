import sys

k=int(sys.stdin.readline())
stack=[]
def push(n):
    stack.append(n)
def pop():
    stack.pop()
for _ in range(k):
    n=int(sys.stdin.readline())
    if n==0: pop()
    else: push(n)

print(sum(stack))
    