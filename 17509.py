arr = []
D = []
V = []
time = 0
penalty = 0
for _ in range(11):
    arr.extend(map(int,input().split()))

for i in range(0,22,2):
    D.append(arr[i])

for i in range(1,22,2):
    V.append(20*arr[i])

D.sort()

for i in range(11):
    time += D[i]
    penalty += (time + V[i])

print(penalty)
