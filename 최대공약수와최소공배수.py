#최소공약수와 최소공배수 찾기!
#gcd함수를 구현하면 될 것 같다.
def gcd(n,m):
    while n:
        n,m=m%n,n
    return m
def solution(n, m):
    answer = []
    mini=gcd(n,m)
    maxi=(n//mini)*(m//mini)*mini
    
    answer.append(mini)
    answer.append(maxi)
    return answer