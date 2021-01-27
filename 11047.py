num, total = map(int, input().split())
coin = []
for i in range(num):
    coin.append(int(input()))

count = 0
i = 0
if coin[num-1] > total:
    while True:
        if total == 0: break
        if total//coin[i]==0 and i<num:
            count += total//coin[i-1]
            total = total%coin[i-1]
            i=0
            continue
        i+=1
    print(count)
elif coin[num-1] == total:
    print(1)
else:
    #입력받은 K금액이 coin 배열의 마지막, 즉 가장 큰 금액의 동전보다
    #클 때를 생각 못해서 틀렸다.
    count+=total//coin[num-1]
    total = total%coin[num-1]
    
    while True:
        if total == 0: break
        if total//coin[i]==0 and i<num:
            count += total//coin[i-1]
            total = total%coin[i-1]
            i=0
            continue
        i+=1
    print(count)
    