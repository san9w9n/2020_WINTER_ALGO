import sys

n = int(sys.stdin.readline())
heap = [0] * (n+1)
length = 0


def insert(num):
    global length, heap
    length+=1
    child = length
    while child!=1 and heap[child//2] < num:
        heap[child] = heap[child//2]
        child //= 2
    heap[child] = num
    

def delete():
    global length, heap
    ans = 0
    if length==1:
        length = 0
        ans = heap[1]
        heap[1]=0
    else:
        temp = heap[length]
        heap[length] = 0
        length-=1

        parent = 1
        child = 2
        ans = heap[1]

        while child<=length:
            if child<length and heap[child] < heap[child+1]: child+=1
            if heap[child] < temp: break

            heap[parent] = heap[child]
            parent = child
            child *= 2
        heap[parent] = temp

    print(ans)

for i in range(n):
    num = int(sys.stdin.readline())
    
    if num==0: 
        if length==0: print(0)
        else: delete()
    else: insert(num)