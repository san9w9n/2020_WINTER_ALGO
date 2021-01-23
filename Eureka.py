#쵀대 3개의 삼각수( 1, 3, 6, 10, 15 ...) 로 모든 자연수를 표현할 수 있다.
#입력에서 테스트케이스의 개수를 주어주고 자연수를 그만큼 입력해준다.
#정확히 3개의 삼각수의 합으로 그 자연수를 표현할 수 있다면 1, 그렇지 않으면 0

#삼각수 리스트 생성
tri_list = [1]
j=1
k=1
for i in range(1,44):
    k += j+i
    tri_list.append(k)

#1부터 1000까지 있는 배열에서 빼는 걸로 생각을 해보자.

#삼각수 1개
K = [int(x) for x in range(3,1001)]
#삼각수 2개
two_tri_list = []
for x in tri_list:
    for y in tri_list:
        if x+y <= 1000:
            two_tri_list.append(x+y)
two_tri_list = list(set(two_tri_list))

#마지막으로 삼각수 3개를 구하고 K에서 그걸 뺀다.
tri_tri_list = []
for x in tri_list:
    for y in two_tri_list:
        if x+y <= 1000:
            tri_tri_list.append(x+y)
tri_tri_list = list(set(tri_tri_list))

for x in tri_tri_list:
    for y in K:
        if x==y:
            K.remove(y)
            
case = int(input())
array = [] * case

for _ in range(case):
    array.append(int(input()))

for x in array:
    if x in K:
        print(0)
    else:
        print(1)
