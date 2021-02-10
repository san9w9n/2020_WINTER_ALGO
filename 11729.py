import sys
order=[]
def hanoi(go,to):
    order.append("{} {}".format(go,to))
def move(n,start,target):
    if n==1:
        hanoi(start,target)
        return
    move(n-1,start,6-start-target)
    hanoi(start,target)
    move(n-1,6-start-target,target)

N = int(sys.stdin.readline())
move(N,1,3)

print(len(order))
for i in order:
    print(i)