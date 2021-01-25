#재귀호출을 통해 부분수열 문제를 푸는 방법이다.
#문제를 보고 딱 떠오를 정도가 되긴 힘들지만,
#다른 사람들이 이렇게 풀었길래 코드를 분석해보고 한 번 짜보려고 한다.
count=0
def brunch(sum,i):
    #return 값이 없기 때문에 global 변수로 count가 필요하다.
    #재귀함수에서 계속해서 count가 더해질 것이다.
    global count

    #i가 배열의 개수보다 커지면 함수는 종료되어야한다.
    if i == n:
        return
    if sum+arr[i] == s:
        count+=1

    #이제 가지를 치면서 나갈 것이다.
    brunch(sum,i+1)
    brunch(arr[i]+sum,i+1)



n, s = map(int,input().split())
arr = list(map(int,input().split()))

brunch(0,0)

print(count)