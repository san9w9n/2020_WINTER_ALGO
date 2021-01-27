#물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때,
#항승이가 필요한 테이프의 최소 개수를 구하는 프로그램
#적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다.

count = 1
last = 0
n, l = map(int, input().split())
repair = sorted(list(map(int, input().split())))

if l==1:
    print(l*n)
else:
    for i in range(n):
        if i < last: continue
        for j in range(n):
            if j>i:
                if repair[i] + (l-1) < repair[j]:
                    count+=1
                    last = j
                    break
                    
                
    print(count)

