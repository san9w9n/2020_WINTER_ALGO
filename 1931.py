#회의시간에 상관 없이 끝나는 시간이 가장 빠른 것을 넣으면 된다.
r = int(input())
time_table = []
for i in range(r):
    time_table.append(list(map(int,input().split())))

time_table.sort(key=lambda x:(x[1],x[0]))
count = 1
last = 0
i = 0
while True:
    if i==r-1: break
    if time_table[last][1] > time_table[i+1][0]:
        i+=1
    else:
        i+=1
        last = i
        count+=1
    

print(count)