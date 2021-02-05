import sys

T = int(sys.stdin.readline())
arr = []
for i in range(1,15):
    arr.append(i)
for _ in range(T):
    h = int(sys.stdin.readline())
    w = int(sys.stdin.readline())
    temp2 = arr
    temp = temp2[:w]
    for _ in range(h):
        for i in range(w):
            temp[i] = sum(temp2[:i+1])
        temp2 = temp[:w]
    print(temp[-1])    
